from django import forms
from .models import CadastroModel
from django.forms import ModelForm

class CadastroForm(ModelForm):

    class Meta:
        model = CadastroModel
        fields = ['nome','professor']
        error_messages = {
        'nome': {
            'required': ("Informe o nome da atividade."),
        }
    }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data