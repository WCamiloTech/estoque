from django.http import HttpResponse
from django.shortcuts import redirect, render

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
