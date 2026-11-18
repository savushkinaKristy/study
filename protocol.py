"""Small synchronous JSON-RPC client for stdio MCP servers.

A background reader with a timeout avoids a hanging CI when the server exits or
never replies. We do not execute any command supplied by the LLM.
"""
from __future__ import annotations
import json
import os
import queue
import subprocess
import threading
from pathlib import Path

class ProtocolError(RuntimeError):pass


def child_env(project_root:Path)->dict[str,str]:
    """Pass no LLM credentials or GitVerse secrets to local servers."""
    pass_through=('PATH','HOME','LANG','LC_ALL','SYSTEMROOT','WINDIR','TMP','TEMP','TMPDIR')
    out={k:v for k,v in os.environ.items() if k.upper() in pass_through}
    out['PYTHONPATH']=str(project_root)
    out['PYTHONIOENCODING']='utf-8'
    out['PYTHONDONTWRITEBYTECODE']='1'
    return out

class MCPStdio:
    def __init__(self,cmd:list[str],cwd:Path,env:dict[str,str],timeout:float=30.0):
        self.cmd=cmd;self.cwd=cwd;self.env=env;self.timeout=timeout
        self.proc=None;self.counter=0;self.q=queue.Queue()

    def __enter__(self):
        self.proc=subprocess.Popen(self.cmd,cwd=self.cwd,env=self.env,stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,stderr=__import__('sys').stderr,
                                   encoding='utf-8',errors='replace',bufsize=1)
        threading.Thread(target=self._reader,daemon=True).start()
        try:
            self.rpc('initialize',{'protocolVersion':'2025-06-18','capabilities':{},
                                   'clientInfo':{'name':'teacher-mcp-orchestrator','version':'1.0.0'}})
            self._send({'jsonrpc':'2.0','method':'notifications/initialized'})
        except Exception:
            self.__exit__(None,None,None);raise
        return self

    def _reader(self):
        try:
            for line in self.proc.stdout:
                if line.strip(): self.q.put(line)
        finally:self.q.put(None)

    def __exit__(self,*_):
        if self.proc:
            if self.proc.poll() is None:
                self.proc.terminate()
                try:self.proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    self.proc.kill();self.proc.wait(timeout=2)
            for stream in (self.proc.stdin,self.proc.stdout):
                if stream:stream.close()

    def _send(self,obj:dict):
        if not self.proc or self.proc.poll() is not None:raise ProtocolError('MCP process exited')
        self.proc.stdin.write(json.dumps(obj,ensure_ascii=False)+'\n');self.proc.stdin.flush()

    def rpc(self,method:str,params:dict|None=None)->dict:
        self.counter+=1;mid=self.counter
        self._send({'jsonrpc':'2.0','id':mid,'method':method,'params':params or {}})
        for _ in range(15):
            try:line=self.q.get(timeout=self.timeout)
            except queue.Empty:raise ProtocolError('Timeout waiting for MCP '+method) from None
            if line is None:raise ProtocolError('MCP process closed stdout during '+method)
            try:response=json.loads(line)
            except json.JSONDecodeError:raise ProtocolError('Invalid JSON on MCP stdout') from None
            if response.get('id') != mid:continue
            if 'error' in response:raise ProtocolError('MCP RPC error: '+str(response['error'])[:250])
            return response['result']
        raise ProtocolError('No matching JSON-RPC message for '+method)

    def list_tools(self):
        tools=[];cursor=None
        for _ in range(10):
            response=self.rpc('tools/list', {'cursor':cursor} if cursor else {})
            tools.extend(response.get('tools',[]))
            cursor=response.get('nextCursor')
            if not cursor:break
        return tools

    def call(self,name:str,args:dict)->dict:
        return self.rpc('tools/call',{'name':name,'arguments':args})


def content_text(result:dict)->str:
    parts=[str(i.get('text','')) for i in result.get('content',[]) if i.get('type')=='text']
    if parts:return '\n'.join(parts)
    if result.get('structuredContent') is not None:return json.dumps(result['structuredContent'],ensure_ascii=False)
    return '{}'


def content_json(result:dict):
    text=content_text(result)
    try:return json.loads(text)
    except json.JSONDecodeError:raise ProtocolError('Expected JSON structured result from own MCP') from None

class MCPRemoteHTTP:
    """Streamable HTTP MCP client, restricted to known endpoints and read-only tools.

    This client never executes remote content, redirects secrets to other hosts,
    or returns the Authorization header to callers. Live network tests belong in CI.
    """
    ENDPOINTS={
        'context7':'https://mcp.context7.com/mcp',
        'gitverse':'https://mcp.gitverse.ru',
    }
    def __init__(self,provider:str,token:str='',timeout:float=45.0):
        if provider not in self.ENDPOINTS:raise ProtocolError('Unapproved remote MCP host')
        if provider=='gitverse' and not token:raise ProtocolError('MCP_GITVERSE_TOKEN is required for live GitVerse')
        self.provider=provider;self.url=self.ENDPOINTS[provider]
        self.token=token;self.timeout=timeout;self.session_id=None;self.version=None;self.mid=0

    def __enter__(self):
        proposed='2024-11-05' if self.provider=='gitverse' else '2025-06-18'
        response=self._rpc('initialize',{'protocolVersion':proposed,
                  'capabilities':{},'clientInfo':{'name':'teacher-mcp-lab','version':'1.1.0'}})
        self.version=response.get('protocolVersion',proposed)
        self._rpc('notifications/initialized',{},notification=True)
        return self

    def __exit__(self,*_):
        self.token=''  # do not persist sensitive material

    def _rpc(self,method:str,params:dict,notification:bool=False):
        from urllib import request,error
        payload={'jsonrpc':'2.0','method':method,'params':params}
        if not notification:
            self.mid+=1;payload['id']=self.mid
        headers={'Content-Type':'application/json','Accept':'application/json, text/event-stream',
                 'User-Agent':'gitverse-mcp-teacher-lab/1.1'}
        if self.token:headers['Authorization']='Bearer '+self.token
        if self.session_id:headers['Mcp-Session-Id']=self.session_id
        if self.version:headers['MCP-Protocol-Version']=self.version
        # No arbitrary URLs: only static, reviewed MCP endpoints are used.
        req=request.Request(self.url,data=json.dumps(payload,ensure_ascii=False).encode('utf-8'),
                            headers=headers,method='POST')
        class NoRedirect(request.HTTPRedirectHandler):
            def redirect_request(self,req,fp,code,msg,headers,newurl):
                raise ProtocolError('Remote MCP redirect refused')
        try:
            opener=request.build_opener(NoRedirect)
            with opener.open(req,timeout=self.timeout) as resp:
                if resp.headers.get('Mcp-Session-Id'):
                    self.session_id=resp.headers.get('Mcp-Session-Id')
                kind=resp.headers.get('Content-Type','')
                raw=resp.read(2_000_001)
        except error.HTTPError as exc:
            raise ProtocolError(f'{self.provider} MCP HTTP {exc.code} ({method}); check token and tool access') from None
        except (error.URLError,TimeoutError) as exc:
            raise ProtocolError(f'{self.provider} MCP network error ({method}): {type(exc).__name__}') from None
        if notification:return {}
        if len(raw)>2_000_000:raise ProtocolError('Remote MCP response too large')
        if 'text/event-stream' in kind:
            messages=[];buf=[]
            for line in raw.decode('utf-8',errors='replace').splitlines():
                if line.startswith('data:'):buf.append(line[5:].lstrip())
                elif not line.strip() and buf:
                    try:messages.append(json.loads('\n'.join(buf)))
                    except json.JSONDecodeError:pass
                    buf=[]
            if buf:
                try:messages.append(json.loads('\n'.join(buf)))
                except json.JSONDecodeError:pass
            matches=[x for x in messages if isinstance(x,dict) and x.get('id')==payload['id']]
            if not matches:raise ProtocolError('No matching JSON-RPC message in MCP event stream')
            data=matches[-1]
        else:
            try:data=json.loads(raw)
            except (ValueError,UnicodeDecodeError):raise ProtocolError('Invalid remote MCP JSON') from None
        if not isinstance(data,dict) or data.get('id')!=payload['id']:
            raise ProtocolError('Incorrect remote MCP response ID')
        if 'error' in data:raise ProtocolError('Remote MCP RPC error (details withheld)')
        if not isinstance(data.get('result'),dict):raise ProtocolError('Remote MCP result missing')
        return data['result']

    def list_tools(self):
        tools=[];cursor=None
        for _ in range(10):
            result=self._rpc('tools/list',{'cursor':cursor} if cursor else {})
            tools.extend(result.get('tools',[]));cursor=result.get('nextCursor')
            if not cursor:break
        return tools

    def call(self,name:str,args:dict):
        allowed={'context7':{'resolve-library-id','query-docs'},
                 'gitverse':{'get_repository','get_repository_content','list_branches','actions_list'}}[self.provider]
        if name not in allowed:raise ProtocolError('Remote write/non-allowlisted tool denied')
        return self._rpc('tools/call',{'name':name,'arguments':args})
