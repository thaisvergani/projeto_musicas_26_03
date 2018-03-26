# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count
from .models import Albums, Musics, Artist
# Create your views here.

def list_albums(request):

    todos_albums = Albums.objects.all()

    return render(request=request,
           template_name="albums.html",
           context={
               "albums" : todos_albums
           })

def albums_details(request, album_id):

    album_obj = Albums.objects.get(pk=album_id)
    musics = album_obj.musics_set.all()

    return render(request=request,
           template_name="album_details.html",
           context={
               "album": album_obj,
               "musics":   musics
           })

def list_artists(request):

    l = Artist.objects
    l = l.annotate(contagem_de_albums=Count("albums"))
    l = l.order_by('contagem_de_albums')
    l = l[:1]
    return render(request=request,
           template_name="artists.html",
           context={
               "artists" : l
           })



