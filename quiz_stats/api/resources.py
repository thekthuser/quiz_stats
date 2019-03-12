# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from tastypie import fields as tasty_fields
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from api.models import Project, Token, Question, Relationship, Answer
from api.authorization import AdminAuthorization, TokenAuthorization, QuestionAuthorization

class ProjectResource(ModelResource):
  class Meta:
    queryset = Project.objects.all()
    resource_name = 'project'
    authentication = BasicAuthentication()
    authorization = AdminAuthorization()

class TokenResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True, null=True)
  class Meta:
    queryset = Token.objects.all()
    resource_name = 'token'
    include_resource_uri = False
    authentication = BasicAuthentication()
    authorization = TokenAuthorization()

class QuestionResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  class Meta:
    queryset = Question.objects.all()
    resource_name = 'question'
    include_resource_uri = False
    authentication = BasicAuthentication()
    authorization = QuestionAuthorization()

class RelationshipResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  question_id = tasty_fields.ForeignKey(QuestionResource, attribute='question_id', full=True)
  token_id = tasty_fields.ForeignKey(TokenResource, attribute='token_id')
  class Meta:
    queryset = Relationship.objects.all()
    resource_name = 'relationship'
    include_resource_uri = False
    authentication = BasicAuthentication()
    authorization = AdminAuthorization()

class AnswerResource(ModelResource):
  project_id = tasty_fields.ForeignKey(ProjectResource, attribute='project_id', full=True)
  question_id = tasty_fields.ForeignKey(QuestionResource, attribute='question_id', full=True)
  class Meta:
    queryset = Answer.objects.all()
    resource_name = 'answer'
    include_resource_uri = False

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'auth/user'
    excludes = ['email', 'password', 'is_superuser']
    authentication = BasicAuthentication()
