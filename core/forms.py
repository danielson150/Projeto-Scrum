from django.forms import ModelForm
from core.models import *


class FormularioCadastroConfeiteiro(ModelForm):
    class Meta:
        model = Confeiteiro
        fields = ['nome', 'login', 'senha', 'email']
        exclude = ['']
