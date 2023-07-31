
# 
from django import template

from PRODUCTManager.models import PRODUCTAList


register = template.Library()

@register.inclusion_tag("template/TAGS/ReplyAnswerList.html",)
def replyANSWERList(q, total):
    try:
        REPLYList = PRODUCTAList.objects.select_related('q', 'user').filter(q_id=q)[:total]
        context = {
            'REPLYANSWERList': REPLYList
        }
        return context
    except PRODUCTAList.DoesNotExist:
        return 'Error Occured'
