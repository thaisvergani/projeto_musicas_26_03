# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Albums(models.Model):
    nome = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.nome

class Musics(models.Model):
    nome = models.CharField(max_length=300)
    albums = models.ForeignKey(Albums)

    def __str__(self):
        return self.nome
