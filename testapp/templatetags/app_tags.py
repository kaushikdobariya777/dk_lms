from django.template import Library
import datetime
register = Library()

@register.simple_tag(name="get_date")
def get_date():
    now = datetime.datetime.now()
    return now

@register.filter
def quotes(value):
    s= '"' + str(value) + '"'
    return s
