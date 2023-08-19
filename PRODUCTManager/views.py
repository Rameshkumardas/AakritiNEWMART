from AdminAuthentication.models import AdminRegistration
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import Http404

class draftPRODUCT(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/orders/orderSTATUS.html'
    ordering = ['id']    
    extra_context = { 'PRODUCTManager':'menu-open', 'draftPRODUCT': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context


class activePRODUCT(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/orders/orderSTATUS.html'
    ordering = ['id']    
    extra_context = { 'PRODUCTManager':'menu-open', 'activePRODUCT': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context
    
class OutOfStockPRODUCT(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/orders/orderSTATUS.html'
    ordering = ['id']    
    extra_context = { 'PRODUCTManager':'menu-open', 'OutOfStockPRODUCT': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context
    

    
class deactivatePRODUCT(ListView):
    model = Blog
    paginate_by = 5
    template_name = './template/orders/orderSTATUS.html'
    ordering = ['id']    
    extra_context = { 'PRODUCTManager':'menu-open', 'deactivatePRODUCT': 'active', 'show':'ALLBlogs'}

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Blogs'] = Blog.objects.all()
        # (is_active=False, is_verfified=False, is_draft=True, )
        return context    