from django import forms
from .models import Aluguel, Livro


class FormAluguel(forms.ModelForm):

    class Meta:
        model = Aluguel
        fields = '__all__'

        widgets = {'livro': forms.CheckboxSelectMultiple}