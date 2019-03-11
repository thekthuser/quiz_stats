from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

class UserObjectsOnlyAuthorization(Authorization):
  def read_list(self, object_list, bundle):
    # This assumes a ``QuerySet`` from ``ModelResource``.
    return object_list.filter(user=bundle.request.user)
  def read_detail(self, object_list, bundle):
    # Is the requested object owned by the user?
    return bundle.obj.user == bundle.request.user
  def create_list(self, object_list, bundle):
    # Assuming they're auto-assigned to ``user``.
    return object_list
  def create_detail(self, object_list, bundle):
    return bundle.obj.user == bundle.request.user
  def update_list(self, object_list, bundle):
    allowed = []
    # Since they may not all be saved, iterate over them.
    for obj in object_list:
      if obj.user == bundle.request.user:
        allowed.append(obj)
    return allowed
  def update_detail(self, object_list, bundle):
    return bundle.obj.user == bundle.request.user
  def delete_list(self, object_list, bundle):
    # Sorry user, no deletes for you!
    raise Unauthorized("Sorry, no deletes.")
  def delete_detail(self, object_list, bundle):
    raise Unauthorized("Sorry, no deletes.")

class AdminAuthorization(Authorization):
  def read_list(self, object_list, bundle):
    if bundle.request.user.is_superuser:
      return object_list
    raise Unauthorized('Unauthorized')
  def read_detail(self, object_list, bundle):
    if bundle.request.user.is_superuser:
      return True
    return False
  def create_list(self, object_list, bundle):
    if bundle.request.user.is_superuser:
      return object_list
    raise Unauthorized('Unauthorized')
  def create_detail(self, object_list, bundle):
    if bundle.request.user.is_superuser:
      return True
    return False
  def update_list(self, object_list, bundle):
    allowed = []
    # Since they may not all be saved, iterate over them.
    for obj in object_list:
      if bundle.request.user.is_superuser:
        allowed.append(obj)
    return allowed
  def update_detail(self, object_list, bundle):
    if bundle.request.user.is_superuser:
      return True
    return False
  #TODO: delete list and detail
