from django.shortcuts import render

def book_detail(request):
    # Словарь с данными о книге
    book = {
        'title': 'Капитанская дочка',
        'author': 'Александр Пушкин',
        'year': 1836,
    }
    # Рендерим шаблон и передаем данные
    return render(request, 'catalog/book_detail.html', {'book': book})
