# Generated by Django 4.1.7 on 2023-03-06 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0002_recette_slug_alter_recette_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
