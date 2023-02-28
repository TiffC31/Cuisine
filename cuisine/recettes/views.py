from multiprocessing import context
from django.shortcuts import render
from django.views import generic
from .models import Recette, Categorie

def Index(request):
    context = {}
    return render(request, 'recettes/index.html', context)

class Categories(generic.ListView):
    model = Categorie
    template_name = 'recettes/categories.html'

class RecettesByCategorie(generic.ListView):
    template_name = 'recettes/recettes_by_categorie.html'

    def get_queryset(self):
        return Recette.objects.filter(categorie__id=self.kwargs['categorie_id'])