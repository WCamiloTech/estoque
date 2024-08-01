# estoque/forms.py
from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  # Inclui todos os campos do modelo no formulário
