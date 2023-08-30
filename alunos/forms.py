from django import forms
from .models import Endereco, Aluno


class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'bairro', 'cep', 'cidade', 'estado']


class FormAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'data_nascimento', 'telefone', 'email']
        exclude = ['endereco']
