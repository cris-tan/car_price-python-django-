from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='dict')
def dict(value, arg):
    try:
        return value[arg]
    except:
        return

@register.filter(name='get_title')
def get_title(value):
    return value.title

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg

@register.filter(name='currency')
def currency(dollars):
    try:
        dollars = round(float(dollars), 0)
        return "%s" % intcomma(int(dollars))
    except:
        return "---"

@register.filter(name='getFloat')
def getFloat(value):
    return float(value)

@register.filter(name='canonicalUrl')
def canonicalUrl(value):
    return value.split("?")[0]

@register.filter(name='postfix')
def postfix(value, arg):
    return value + arg

