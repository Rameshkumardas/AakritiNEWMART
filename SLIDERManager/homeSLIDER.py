from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .models import BANNERLists
from django.contrib import messages

class HOMEBANNERLists(ListView):
    paginate_by = 5
    template_name = './templates/blog/all-blogs.html'
    ordering = ['id'] 
    context_object_name = 'BANNERLists'
    extra_context = { 'SLIDERManager':'menu-open', 'BANNER': 'active'}
    def get_queryset(self, *args, **kwargs):
        return BANNERLists.objects.filter(is_active=True, is_verified=True)