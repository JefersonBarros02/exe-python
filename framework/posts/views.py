from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
    return render(request, 'posts.html')

def cadastro(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
        'msg': 'Pedido efetuado com sucesso!'
        }

        return render(request, 'cadastro.html', context)

    context = {
        'formulario': form
    }

    return render(request, 'cadastro.html', context)