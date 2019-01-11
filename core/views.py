from django.shortcuts import render
from core.forms import *
from core.models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')


def cadastrar(request):
    return render(request, 'cadastro.html')


# Metodos para a gerencia de confeiteiros
def seleciona_todos_os_confeiteiros_cadastrados():
    return Confeiteiro.objects.all()


def cadastrar_novo_confeiteiro(nome, email, senha, contato):
    confeiteiro = Confeiteiro(nome=nome, email=email, senha=senha, contato=contato)
    confeiteiro.save()


def selecionar_confeiteiro_por_id(id):
    return Confeiteiro.objects.all().filter(id=id)


def deletar_confeiteiro_por_id(pk):
    confeiteiro = Confeiteiro.objects.get(pk=pk)
    confeiteiro.delete()
