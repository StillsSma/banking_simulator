from rest_framework import permissions

class IsCreatedBy(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.account)
        print(request.user.profile)
        return obj.account == request.user.profile

class Post(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(23)
        print(request)
