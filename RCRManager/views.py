from AdminAuthentication.models import AdminRegistration
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import Http404
from Blogs.models import Blog


class RCRReturnedORDERS(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/ReturnedSTATUS.html'
    ordering = ['id']    
    extra_context = { 'RCRManager':'menu-open', 'ReturnedSTATUS': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context

class RCRCancelledORDERS(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/CancelledSTATUS.html'
    ordering = ['id']    
    extra_context = { 'RCRManager':'menu-open', 'CancelledSTATUS': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context

class RCRReplacedORDERS(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/ReplacedSTATUS.html'
    ordering = ['id']    
    extra_context = { 'RCRManager':'menu-open', 'ReplacedSTATUS': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context


