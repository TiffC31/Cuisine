from django.urls import path
from . import views

app_name = "recettes"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:categorie_id>/', views.Liste.as_view(), name='recettes_by_categorie'),
]