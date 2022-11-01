from multiprocessing import context
from django.shortcuts import render
from django.views import generic
from .models import Recette, Categorie

def Index(request):
    context = {}
    return render(request, 'recettes/index.html', context)

class MesRecettes(generic.ListView):
    model = Recette
    paginate_by = 25
    template_name = 'recettes/mes_recettes.html'

#     def get_queryset(self):
#         return Recette.objects.order_by('titre')


# class DetailView(generic.DetailView):
#     model = Recette
#     template_name = 'recettes/fiche.html'


# class ListView(generic.ListView):
#     model = Recette
#     template_name = 'recettes/liste.html'