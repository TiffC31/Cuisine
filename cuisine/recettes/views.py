from django.shortcuts import render, redirect
from multiprocessing import context
from django.views.generic import View, ListView
from .models import Recette, Categorie
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin, ListView):
    model = Categorie
    template_name = 'recettes/liste.html'

    def get_queryset(self):
        return Categorie.objects.order_by('tri')

class Liste(LoginRequiredMixin, ListView):
    template_name = 'recettes/liste.html'
    paginate_by = 12

    def get_queryset(self):
        return Recette.objects.filter(categorie__slug=self.kwargs['slug'])

    def get_context_data(self,**kwargs):
        context = super(Liste,self).get_context_data(**kwargs)
        context['categorie_list'] = Categorie.objects.order_by('tri')
        context['slug'] = self.kwargs['slug']
        return context
    
class RecetteCreateView(View):
    form_class = forms.CreateForm
    template = 'recettes/recette_create_form.html'

    def get(self, request):
        return render(request, self.template, context={'form':self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if (form.is_valid()):
            recette = form.save(commit=False)
            recette.user_id = request.user.id
            recette.save()
            return redirect('recettes:index')
        else:
            return render(request, self.template, context={'form':form})