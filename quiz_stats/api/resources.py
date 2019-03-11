# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from api.models import Project, Token, Question, Relationship, Answer

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

class RelationshipResource(ModelResource):
  class Meta:
    queryset = Relationship.objects.all()
    resource_name = 'relationship'

class AnswerResource(ModelResource):
  class Meta:
    queryset = Answer.objects.all()
    resource_name = 'answer'
