# Custom template tags for G-Scores
from django import template

register = template.Library()


@register.filter
def div(value, arg):
    """Divide value by arg"""
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0


@register.filter
def mul(value, arg):
    """Multiply value by arg"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def percentage(value, total):
    """Calculate percentage"""
    try:
        if total > 0:
            return (float(value) / float(total)) * 100
        return 0
    except (ValueError, ZeroDivisionError):
        return 0