from django.shortcuts import redirect, render

from .forms import ProdutoForm
from .models import Produto

# Create your views here.
# estoque/views.py

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nome_da_url_para_lista_de_produtos')  # Substitua pelo nome da URL de destino
    else:
        form = ProdutoForm()
    
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

def home(request):
    return render(request, 'estoque/home.html')