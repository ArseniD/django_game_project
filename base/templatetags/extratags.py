import datetime

from django import template

register = template.Library()


@register.filter(name='range')
def get_range(value):
    return xrange(value)


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(name='asterisk')
def cut(value):
    """Removes all values of arg from the given string"""
    return str('*****************')

