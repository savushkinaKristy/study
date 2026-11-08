from django.shortcuts import render
from datetime import datetime

def post_list(request):
    # Пример данных (в реальном проекте - из базы данных)
    posts = [
        {
            'title': 'Мой первый пост',
            'content': 'Это содержание моего первого поста в блоге. Здесь я рассказываю о том, как начал изучать Django.',
            'published_date': datetime(2024, 1, 15),
            'author': 'ADMIN'
        },
        {
            'title': 'Второй пост о Django',
            'content': 'Во втором посте я хочу поделиться впечатлениями о работе с шаблонами Django. Это очень удобно!',
            'published_date': datetime(2024, 1, 20),
            'author': 'AUTHOR'
        }
    ]
    # Рендерим шаблон и передаем данные в контексте
    return render(request, 'posts/post_list.html', {'posts': posts})

def about(request):
    return render(request, 'posts/about.html')
