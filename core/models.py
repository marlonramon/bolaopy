# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clube(models.Model):

    nome = models.CharField(max_length=255, null=False)
    bandeira = models.CharField(max_length=255, null=False)
