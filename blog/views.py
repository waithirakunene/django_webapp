# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #display from the database
    content = { 
    "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', content)

def about(request):
    return render(request, 'blog/about.html')#{'title':'about'})
