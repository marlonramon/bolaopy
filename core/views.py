# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from core.models import Clube
from core.forms import ClubeForm

def index(request):
    return render(request, 'index.html')

def clubes(request):

    clubes = Clube.objects.all()

    return render(request,'clube/list-clubes.html', {'clubes': clubes})

def clube_new(request):
    
    if request.method == "POST":
        form = ClubeForm(request.POST)
        if form.is_valid():
            clube = form.save(commit=False)
            clube.save()
            return redirect('clube_detail', pk=clube.pk)
    else:
        form = ClubeForm()
    return render(request, 'clube/clube_edit.html', {'form': form})    