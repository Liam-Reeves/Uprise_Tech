from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='about.html')


def products(request):
    return render(request, template_name='products.html')


def contact(request):
    return render(request, template_name='contact.html')

