from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def percentage(value, arg):
    try:
        # Converte os valores para Decimal
        value = Decimal(value)
        arg = Decimal(arg)
        return int((value * Decimal('100.0')) // arg)
    except (ValueError, ZeroDivisionError):
        return 0
