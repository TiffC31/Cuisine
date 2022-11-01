from django.urls import path
from . import views

app_name = "recettes"
urlpatterns = [
    path('', views.Index, name='index'),
    path('mes_recettes/', views.MesRecettes.as_view(), name='mes_recettes'),
    # path('liste/', views.ResultsView.as_view(), name='liste'),
]