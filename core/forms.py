from django.forms import ModelForm
from core.models import *


class FormularioCadastroConfeiteiro(ModelForm):
    class Meta:
        model = Confeiteiro
        fields = ['nome', 'login', 'senha', 'email']
        exclude = ['']


class FormularioContatoConfeiteiro(ModelForm):
    class Meta:
        model = ContatoConfeiteiro
        exclude = ['confeitero']


class FormularioCadastroCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'login', 'Senha']
        exclude = ['']


class FormularioCadastroServico(ModelForm):
    class Meta:
        model = Postagem
        exclude = ['confeitero']


class FormularioContatoCliente(ModelForm):
    class Meta:
        model = ContatoCliente
        exclude = ['cliente']


class FormularioPublicacaoCliente(ModelForm):
    class Meta:
        model = ClientePublicacao
        exclude = ['cliente']


class FormularioAvalizacao(ModelForm):
    class Meta:
        model = Avaliacao
        exclude = ['confeitero', 'cliente']
