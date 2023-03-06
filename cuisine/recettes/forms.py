from django import forms
from .models import Recette

class CreateForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = '__all__'