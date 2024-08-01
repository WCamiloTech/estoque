# /estoque/urls.py
from django.urls import path

from .views import adicionar_produto

urlpatterns = [
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
]
