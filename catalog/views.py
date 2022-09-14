from msilib.schema import Class
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Service

# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'
    login_url = '/login'

class CategoryView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'obj'
    login_url = 'login'

class ServiceView(LoginRequiredMixin, generic.ListView):
    model = Service
    template_name = 'catalog/service_list.html'
    context_object_name = 'obj'
    login_url = 'login'
