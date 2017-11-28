# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from gallery.models import *


class category_admin(admin.ModelAdmin):
	pass
admin.site.register(Category, category_admin)


class Gallery_Admin(admin.ModelAdmin):
	list_display = ('alt', 'text','small','cate', 'PHOTO', 'reg')
admin.site.register(Gallery, Gallery_Admin)