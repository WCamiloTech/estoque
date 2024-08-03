from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProdutoForm
from .models import Produto


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona para a view 'home' após adicionar o produto
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

def home(request):
    produtos = Produto.objects.all()  # Busca todos os produtos cadastrados
    return render(request, 'estoque/home.html', {'produtos': produtos})

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')  # Substitua 'home' pela URL onde você deseja redirecionar após a atualização
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'estoque/atualizar_produto.html', {'form': form})

def remover_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto removido com sucesso.')
        return redirect(reverse('home'))  # Substitua 'home' pela URL para a qual você deseja redirecionar após a remoção
    
    # Se você quiser uma página de confirmação antes da remoção, renderize um template aqui
    return render(request, 'estoque/confirmar_remocao.html', {'produto': produto})
