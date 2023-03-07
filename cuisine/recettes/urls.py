from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "recettes"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('categorie/<slug:slug>/', views.Liste.as_view(), name='recettes_by_categorie'),
    path('nouvelle/', views.RecetteCreateView.as_view(), name='nouvelle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)