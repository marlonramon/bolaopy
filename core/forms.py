from django import forms
from core.models import Clube


class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = ('nome','bandeira')

        widgets = {
            'nome' : forms.TextInput(attrs={'id':'nome' ,'class': 'form-control'}),
            'bandeira' : forms.TextInput(attrs={'id':'bandeira' ,'class': 'form-control'})
        }


