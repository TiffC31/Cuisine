import datetime
from pickle import TRUE
from django.db import models
from django.utils import timezone
from  django.urls  import  reverse
from common.utils.slug import slug_unique
from django.contrib.auth import get_user_model

UNITES = [('g', 'grammes'),
          ('kg', 'kilogrammes'),
          ('l', 'litres'),
          ('ml', 'millilitres'),
          ('cl', 'centilitres'),
          ('cac', 'c. à café'),
          ('cas', 'c. à soupe')]

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
    COUTS = [(1, 'Bon marché'), (2, 'Abordable'), (3, 'Assez cher')]
    DIFFICULTES = [(1, 'Très facile'), (2, 'Facile'), (3, 'Intermédiaire'), (4, 'Difficile')]
    UNITES.insert(0, ('pers', 'personnes'))
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='recettes/', null=True, blank=True, default='recettes/no-image.jpg')
    tps_preparation_h = models.PositiveSmallIntegerField(null=True, blank=True)
    tps_preparation_m = models.PositiveSmallIntegerField(null=True, blank=True)
    tps_cuisson_h = models.PositiveSmallIntegerField(null=True, blank=True)
    tps_cuisson_m = models.PositiveSmallIntegerField(null=True, blank=True)
    tps_repos_h = models.PositiveSmallIntegerField(null=True, blank=True)
    tps_repos_m = models.PositiveSmallIntegerField(null=True, blank=True)
    cout = models.PositiveSmallIntegerField(choices=COUTS, null=True, blank=True)
    difficulte = models.PositiveSmallIntegerField(choices=DIFFICULTES, null=True, blank=True)
    quantite = models.PositiveSmallIntegerField(null=True, blank=True)
    unite_quantite = models.CharField(choices=UNITES, max_length=5, null=True, blank=True)
    commentaire = models.TextField(null=False, blank=True)
    modifie_le = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, unique=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('recette-detail', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slug_unique(self.titre, Recette.objects, self.id)
        return super(Recette, self).save(*args, **kwargs)
