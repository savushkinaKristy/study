from django.shortcuts import render

def book_detail(request):
    # Словарь с данными о книге
    book = {
        'title': 'Капитанская дочка',
        'author': 'Александр Пушкин',
        'year': 1836,
        'price': 1500,
    }
    # Рендерим шаблон и передаем данные
    return render(request, 'catalog/book_detail.html', {'book': book})


def book_list(request):
    """
    Отображает страницу со списком всех книг.

    Args:
        request (HttpRequest): Объект HTTP-запроса от клиента.

    Returns:
        HttpResponse: Отрендеренный HTML-шаблон 'catalog/book_list.html'
                      с переданным контекстом (списком книг).
    """
    # Создаем список из нескольких книг
    books = [
        {
            'title': 'Капитанская дочка',
            'author': 'Александр Пушкин',
        },
        {
            'title': 'Мастер и Маргарита',
            'author': 'Михаил Булгаков',
        },
        {
            'title': 'Преступление и наказание',
            'author': 'Федор Достоевский',
        }
    ]
    return render(request, 'catalog/book_list.html', {'books': books})
