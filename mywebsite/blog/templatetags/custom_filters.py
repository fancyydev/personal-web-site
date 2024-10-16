from django import template

register = template.Library()

@register.filter
def split_by_comma(value):
    """Split the string by commas and return a list."""
    return value.split(',')
