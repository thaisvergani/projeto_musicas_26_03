# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Artist, Albums, Musics
# Register your models here.

admin.site.register(Artist)
admin.site.register(Albums)
admin.site.register(Musics)