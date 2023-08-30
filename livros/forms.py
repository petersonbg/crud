from django import forms
from livros.models import Categorias, Livro


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categoria']


class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'categoria', 'descricao']
        widgets = {
            'titulo': forms.TextInput,
            'autor': forms.TextInput,
            'editora': forms.TextInput,
            'categoria': forms.Select,
            'descricao': forms.Textarea
        }
