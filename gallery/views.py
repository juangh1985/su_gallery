# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.http import HttpRequest  
from django.db.models import Count
# Create your views here.

from gallery.models import *
import socket


import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def galeria(request):

	g = Gallery.objects.all().order_by('-src')
	c = Category.objects.all().annotate(number=Count('gallery')).order_by('cate')

	if request.method == 'GET':
		getimage = request.GET.get ('i')
		getvote = request.GET.get ('v')
		if getimage:
			img = Gallery.objects.get(id=getimage)
			if getvote == "1":
				img.counterup = int(img.counterup) + int(getvote)
				img.save()
			elif getvote == "-1":
				img.counterdown = int(img.counterdown) + int(getvote)
				img.save()

			voterecord = Vote(gal=img, cou=int(getvote))
			voterecord.save()
			return HttpResponseRedirect('/galeria')


	if request.method == 'POST':
		getcategory = request.POST.get ('c')
		if getcategory:
			catselect = Category.objects.get(id=getcategory)
			g = Gallery.objects.filter(cate=catselect).order_by('-src')
			c = Category.objects.all().annotate(number=Count('gallery')).order_by('cate')

			context = {
			'gallery':g,
			'catselect':catselect,
			'category':c,
			}
			return render(request, 'gallery.html', context)


	context = {
	'gallery':g,
	'category':c,
	}
	return render(request, 'gallery.html', context)

