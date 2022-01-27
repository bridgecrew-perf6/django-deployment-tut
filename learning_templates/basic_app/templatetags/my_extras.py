from django import template

register = template.Library()

@register.filter
def cut(value,arg):
    """
    this cuts out all values of 'arg' from the sting
    """
    return value.replace(arg,'')

