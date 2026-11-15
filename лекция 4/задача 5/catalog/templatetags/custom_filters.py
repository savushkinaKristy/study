from django import template

register = template.Library()

@register.filter
def format_currency(value):
    return f"{value} р"