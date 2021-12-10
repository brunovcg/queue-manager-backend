from rest_framework.permissions import BasePermission

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):  
  
        return (request.user.is_staff == True and request.user.is_superuser == True)


class IsStaff(BasePermission):
    def has_permission(self, request, view):
  
        return (request.user.is_staff == True)


class IsSuperuserStaffCanGet(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET': 
            return (request.user.is_staff == True)

        return (request.user.is_superuser == True)


class IsUserOrSuperuser(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser == True:
            return True

        return (request.user.is_staff == False and request.user.is_superuser == False)

class SuperuserGetForAll(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET': 
            return True

        return (request.user.is_superuser == True)

