import datetime
from pickle import TRUE
from django.db import models
from django.utils import timezone
from  django.urls  import  reverse
from common.utils.slug import slug_unique

class Categorie(models.Model):
    nom = models.CharField(max_length=20)
    modifie_le = models.DateTimeField(auto_now=True)
    tri = models.IntegerField(unique=True, null=True)
    slug = models.SlugField(null=False, blank=True, unique=True)
    
    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse('recettes:recettes_by_categorie', kwargs={'slug':self.slug})

class Recette(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='recettes/', null=True, blank=True, default='recettes/no-image.jpg')
    modifie_le = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, unique=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('recette-detail', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slug_unique(self.titre, Recette.objects, self.id)
        return super(Recette, self).save(*args, **kwargs)
