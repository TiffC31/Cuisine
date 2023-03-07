from django.contrib import admin
from .models import Categorie, Recette

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tri')
    prepopulated_fields = {'slug':('nom',)}

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'photo', 'categorie_id')
    prepopulated_fields = {'slug':('titre',)}

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Recette, RecetteAdmin)