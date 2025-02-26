from django.urls import path

from app import views

urlpatterns = [

    path('', views.index, name='index'),

    path('products/', views.products, name='products'),

    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),
]
