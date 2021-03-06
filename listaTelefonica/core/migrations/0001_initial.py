# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-04 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('telefone', models.CharField(max_length=10, null=True)),
                ('data', models.DateField(null=True)),
                ('operadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contato')),
            ],
            options={
                'verbose_name_plural': 'contatos',
                'verbose_name': 'contato',
            },
        ),
        migrations.CreateModel(
            name='Operadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, null=True)),
                ('codigo', models.CharField(max_length=2, null=True)),
                ('categoria', models.CharField(max_length=10, null=True)),
                ('preco', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'operadoras',
                'verbose_name': 'operadora',
            },
        ),
    ]
