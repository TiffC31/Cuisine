from django.urls import path
from . import views

app_name = "recettes"
urlpatterns = [
    path('', views.Index, name='index'),
    path('mes_recettes/', views.Categories.as_view(), name='categories'),
    path('mes_recettes/<int:categorie_id>/', views.RecettesByCategorie.as_view(), name='recettes_by_categorie'),
]