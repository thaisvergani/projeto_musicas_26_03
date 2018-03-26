# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Musics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicas.Albums')),
            ],
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicas.Artist'),
        ),
    ]
