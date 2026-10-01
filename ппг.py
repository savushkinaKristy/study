a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = min(b, c) * 2 + (1 if max(b, c) > min(b, c) else 0) + a + d
print(result)
