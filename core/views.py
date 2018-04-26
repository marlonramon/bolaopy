# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from core.models import Clube
from core.forms import ClubeForm

def index(request):
    return render(request, 'index.html')

def clubes(request, template_name='clube/list-clubes.html'):
    clubes = Clube.objects.all()
    return render(request, template_name, {'clubes': clubes})

def clube_new(request, template_name='clube/clube_form.html'):
    
    if request.method == "POST":
        form = ClubeForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Clube inserido com sucesso!')
            return redirect('clube_list')
    else:
        form = ClubeForm()
    return render(request, template_name, {'form': form})    

def clube_update(request, pk , template_name='clube/clube_form.html'):
    
    clube = get_object_or_404(Clube, pk=pk)
    form = ClubeForm(request.POST or None, instance=clube)

    if (form.is_valid()):
        form.save()
        messages.success(request, 'Clube alterado com sucesso!')
        return redirect('clube_list')
    return render(request,template_name, {'form':form})    

def clube_delete(request, pk , template_name='clube/confirm_delete.html'):
    
    clube = get_object_or_404(Clube, pk=pk)
    
    if (request.method == "POST"):
        clube.delete()
        messages.success(request, 'Clube excluido com sucesso!')
        return redirect('clube_list')
    return render(request,template_name, {'clube':clube})        