# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from api.models import Project

class ProjectResource(ModelResource):
  class Meta:
    queryset = Project.objects.all()
    resource_name = 'project'
