# Generated by Django 5.1.4 on 2024-12-16 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fonctionnalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('valide', models.BooleanField(default=False)),
                ('difficulte', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=200, unique=True)),
                ('est_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
                ('statut', models.CharField(default='new', max_length=20)),
                ('mode_jeu', models.CharField(choices=[('strict', 'Strict'), ('moyenne', 'Moyenne')], default='strict', max_length=50)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parties_gerees', to='myapp.participant')),
                ('fonctionnalites', models.ManyToManyField(blank=True, related_name='parties', to='myapp.fonctionnalite')),
                ('participants', models.ManyToManyField(related_name='parties', to='myapp.participant')),
            ],
        ),
        migrations.CreateModel(
            name='ValidationFonctionnalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validée', models.BooleanField(default=False)),
                ('fonctionnalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fonctionnalite')),
                ('partie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.partie')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(max_length=20)),
                ('mode_jeu', models.CharField(choices=[('strict', 'Strict'), ('moyenne', 'Moyenne'), ('mediane', 'Médiane'), ('majorite_absolue', 'Majorité absolue'), ('majorite_relative', 'Majorité relative')], max_length=20)),
                ('fonctionnalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fonctionnalite')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.participant')),
                ('partie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.partie')),
            ],
        ),
    ]
