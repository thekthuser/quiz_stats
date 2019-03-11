# -*- coding: utf-8 -*-

from tastypie import fields as tasty_fields
from tastypie.resources import ModelResource
from api.models import Project, Token, Question, Relationship, Answer

class ProjectResource(ModelResource):
  class Meta:
    queryset = Project.objects.all()
    resource_name = 'project'

class TokenResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  class Meta:
    queryset = Token.objects.all()
    resource_name = 'token'
    include_resource_uri = False

class QuestionResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  class Meta:
    queryset = Question.objects.all()
    resource_name = 'question'
    include_resource_uri = False

class RelationshipResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  question_id = tasty_fields.ForeignKey(QuestionResource, attribute='question_id', full=True)
  token_id = tasty_fields.ForeignKey(TokenResource, attribute='token_id')
  class Meta:
    queryset = Relationship.objects.all()
    resource_name = 'relationship'
    include_resource_uri = False

class AnswerResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  question_id = tasty_fields.ForeignKey(QuestionResource, attribute='question_id', full=True)
  class Meta:
    queryset = Answer.objects.all()
    resource_name = 'answer'
    include_resource_uri = False
