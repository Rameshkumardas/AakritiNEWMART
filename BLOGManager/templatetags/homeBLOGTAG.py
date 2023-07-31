from django import template

from BLOGManager.models import replyBLOGCOMMENTS, replyCHILDBLOGCOMMENTS

register = template.Library()


@register.filter(name='split')
def split(value, key):
    return value.split(key)


@register.inclusion_tag('./template/TAGS/ReplyComment.html',)
def replyCOMMENTList(comment, total):
    try:
        REPLYList = replyBLOGCOMMENTS.objects.select_related('comment', 'author').filter(comment_id=comment)[:total]
        context = {
            'REPLYCOMMENTList': REPLYList
        }
        return context
    except replyBLOGCOMMENTS.DoesNotExist:
        return 'Error Occured'

@register.inclusion_tag('./template/TAGS/replyCHILDCOMMENTList.html',)
def replyCHILDCOMMENTList(comment, total):
    try:
        REPLYCHILDCOMMENTList = replyCHILDBLOGCOMMENTS.objects.select_related('comment', 'author').filter(comment_id=comment)[:total]
        context = {
            'REPLYCHILDCOMMENTList': REPLYCHILDCOMMENTList
        }
        return context
    except replyCHILDBLOGCOMMENTS.DoesNotExist:
        return 'Error Occured'