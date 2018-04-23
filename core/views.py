# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import Clube

def index(request):
    return render(request, 'index.html')

def clubes(request):

    clubes = Clube.objects.all()

    return render(request,'clube/list-clubes.html', {'clubes': clubes})