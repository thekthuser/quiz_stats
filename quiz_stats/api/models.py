# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
  name = models.CharField(max_length=127, default='Untitled Project')
  description = models.CharField(max_length=255, default='')
  is_active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Token(models.Model):
  project = models.ForeignKey(Project)
  name = models.CharField(max_length=127, default='Untitled Token')
  description = models.CharField(max_length=255, default='')
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Question(models.Model):
  project = models.ForeignKey(Project)
  text = models.CharField(max_length=255, default='Dev Question?')
  is_active = models.BooleanField(default=True)
  next_question = models.ForeignKey('self', related_name='prev_question_id', null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Relationship(models.Model):
  project = models.ForeignKey(Project)
  question = models.ForeignKey(Question)
  token = models.ForeignKey(Token)
  value = models.IntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
  project = models.ForeignKey(Project)
  question = models.ForeignKey(Question)
  answer = models.BooleanField(default=True)
  user = models.ForeignKey(User)
  created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
