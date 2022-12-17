from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ProductForm
from .models import Product
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class Index(TemplateView):
    template_name = 'index.html'


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'


class About(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'contacts.html'


class AddProduct(LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    model = Product
    login_url = '/login'
    success_url = '/products'
    form_class = ProductForm


class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'
