# Generated by Django 4.1.7 on 2023-03-03 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('modifie_le', models.DateTimeField(auto_now=True)),
                ('tri', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/recettes')),
                ('modifie_le', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recettes.categorie')),
            ],
        ),
    ]
