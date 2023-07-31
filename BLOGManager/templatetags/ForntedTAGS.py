from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter(name='highlight')
def highlight(text, search):
    highlighted = text.replace(search, '<b class="text bg-warning">{}</b>'.format(search))
    return mark_safe(highlighted)

