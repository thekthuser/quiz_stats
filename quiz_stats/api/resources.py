# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from api.models import Project, Token, Question

class ProjectResource(ModelResource):
  class Meta:
    queryset = Project.objects.all()
    resource_name = 'project'

class TokenResource(ModelResource):
  class Meta:
    queryset = Token.objects.all()
    resource_name = 'token'

class QuestionResource(ModelResource):
  class Meta:
    queryset = Question.objects.all()
    resource_name = 'question'
