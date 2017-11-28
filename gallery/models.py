# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.admin import AdminSite

# Register your models here

class MyAdminSite(AdminSite):
	site_header = 'Sirvase Usted'
	site_title = 'Sirvase Usted'
	index_title = 'Sistema de Control'

admin_site = MyAdminSite(name='myadmin')

from tinymce.models import HTMLField

class Category(models.Model):
	cate=models.CharField('Category',max_length=256)
	acti = models.BooleanField('ActivE', max_length=3, blank=True)
	def __unicode__(self):
		return '%s' % (self.cate)

class Gallery(models.Model):
	alt=models.CharField('alt',max_length=128, blank=True)
	text=models.TextField('text',max_length=512, blank=True)
	src = models.FileField(upload_to='image/%Y/%m/%d/')
	acti = models.BooleanField('active', max_length=3, blank=True)
	small=models.CharField('small',max_length=256)
	cate=models.ForeignKey('category',max_length=256)
	reg=models.DateTimeField('Record',max_length=256, auto_now=True, blank=True)
	counterup=models.IntegerField('Count Up', blank=True, default="0")
	counterdown=models.IntegerField('Count Down', blank=True, default="0")


	def __unicode__(self):
		return '%s' % (self.alt)


	def PHOTO(self):
		return '<img src="/imagenes/%s" width="96" />' % self.src
	PHOTO.allow_tags = True



class Vote(models.Model):
	gal=models.ForeignKey('Gallery',max_length=256)
	cou=models.IntegerField('Count', blank=True)
	reg=models.DateTimeField('Record',max_length=256, auto_now=True, blank=True)
