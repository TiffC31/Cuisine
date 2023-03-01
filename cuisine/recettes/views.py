from multiprocessing import context
from django.shortcuts import render
from django.views import generic
from .models import Recette, Categorie

class Categories(generic.ListView):
    model = Categorie
    template_name = 'recettes/categories.html'

    def get_queryset(self):
        return Categorie.objects.order_by('tri')

class RecettesByCategorie(generic.ListView):
    template_name = 'recettes/recettes_by_categorie.html'

    def get_queryset(self):
        return Recette.objects.filter(categorie__id=self.kwargs['categorie_id'])

    def get_context_data(self,**kwargs):
        context = super(RecettesByCategorie,self).get_context_data(**kwargs)
        context['categorie_list'] = Categorie.objects.order_by('tri')
        context['categorie_id'] = self.kwargs['categorie_id']
        return context