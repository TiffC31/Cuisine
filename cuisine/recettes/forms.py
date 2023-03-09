from django import forms
from .models import Recette

class CreateForm(forms.ModelForm):
    tps_preparation_m = forms.IntegerField(max_value=59)
    tps_cuisson_m = forms.IntegerField(max_value=59)
    tps_repos_m = forms.IntegerField(max_value=59)

    class Meta:
        model = Recette
        exclude = ['user','modifie_le','slug']
        widgets = {
            'commentaire' : forms.Textarea(attrs={'rows' : 3})
        }
        labels = {
            'categorie' : 'Catégorie',
            'tps_preparation_h' : 'Temps de préparation',
            'tps_cuisson_h' : 'Temps de cuisson',
            'tps_repos_h' : 'Temps de repos',
            'cout' : 'Coût',
            'difficulte' : 'Difficulté',
            'quantite' : 'Quantité'
        }