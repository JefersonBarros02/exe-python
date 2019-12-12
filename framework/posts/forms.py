from django import forms
from .models import Formulario

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nome',
            'email',
            'data_nascimento', 
            'senha',
            'confirmacao_senha'
        ]