from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter(name='date')
def show_date(value):
    return date2jalali(value)


@register.filter(name='time')
def show_time(value):
    return value.strftime('%H:%M')
