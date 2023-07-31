
from ..models import BlogMainCat, BlogSubCat
from django import template

register = template.Library()


@register.simple_tag
def BLOGMainCatName(pk):
    mainCat = BlogMainCat.objects.get(pk=pk)
    return mainCat.name

@register.simple_tag
def BLOGSubCatName(pk):
    subCat = BlogSubCat.objects.get(pk=pk)
    return subCat.name


