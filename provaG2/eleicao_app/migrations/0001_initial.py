# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 00:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('dataH_inicio', models.DateTimeField(blank=True, null=True)),
                ('dataH_fim', models.DateTimeField(blank=True, null=True)),
                ('local', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=14)),
                ('eleicao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('senha', models.CharField(max_length=35)),
                ('voto', models.BooleanField(default=False, verbose_name='Candidato votou!?')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('eleicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataH_voto', models.DateTimeField(blank=True, null=True)),
                ('em_branco', models.BooleanField(default=False, verbose_name='Deseja votar em branco!?')),
                ('candidato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Candidato')),
            ],
        ),
        migrations.AddField(
            model_name='eleitor',
            name='token',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Token'),
        ),
        migrations.AddField(
            model_name='eleitor',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='candidato',
            name='eleicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Eleicao'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao_app.Vaga'),
        ),
    ]
