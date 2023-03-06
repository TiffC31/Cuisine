import datetime
from pickle import TRUE
from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=20)
    modifie_le = models.DateTimeField(auto_now=True)
    tri = models.IntegerField(unique=True, null=True)
    def __str__(self):
        return self.nom

class Recette(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='recettes/', null=True, blank=True, default='recettes/no-image.jpg')
    modifie_le = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre
