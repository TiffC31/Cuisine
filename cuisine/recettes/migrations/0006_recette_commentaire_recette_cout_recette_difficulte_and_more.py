# Generated by Django 4.1.7 on 2023-03-08 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recettes', '0005_alter_categorie_slug_alter_recette_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='commentaire',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='cout',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Bon marché'), (2, 'Abordable'), (3, 'Assez cher')], null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='difficulte',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Très facile'), (2, 'Facile'), (3, 'Intermédiaire'), (4, 'Difficile')], null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='quantite',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='tps_cuisson',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='tps_preparation',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='tps_repos',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='unite_quantite',
            field=models.CharField(blank=True, choices=[('pers', 'personnes'), ('g', 'gramme'), ('kg', 'kilogrammes'), ('l', 'litres'), ('ml', 'millilitre'), ('cl', 'centilitre'), ('cac', 'cuillère à café'), ('cas', 'cuillère à soupe')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='recette',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
