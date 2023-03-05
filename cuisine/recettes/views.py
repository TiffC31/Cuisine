from multiprocessing import context
from django.views import generic
from .models import Recette, Categorie
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin, generic.ListView):
    model = Categorie
    template_name = 'recettes/liste.html'

class Liste(LoginRequiredMixin, generic.ListView):
    template_name = 'recettes/liste.html'
    paginate_by = 12

    def get_queryset(self):
        return Recette.objects.filter(categorie__id=self.kwargs['categorie_id'])

    def get_context_data(self,**kwargs):
        context = super(Liste,self).get_context_data(**kwargs)
        context['categorie_list'] = Categorie.objects.order_by('tri')
        context['categorie_id'] = self.kwargs['categorie_id']
        return context