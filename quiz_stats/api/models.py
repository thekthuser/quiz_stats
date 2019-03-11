# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=127, default='Untitled Project')
  description = models.CharField(max_length=255, default='')
  is_active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
