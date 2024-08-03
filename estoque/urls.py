# /estoque/urls.py
from django.urls import path

from .views import adicionar_produto, atualizar_produto, remover_produto

urlpatterns = [
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('produto/atualizar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('produto/remover/<int:pk>/', remover_produto, name='remover_produto'),

]
