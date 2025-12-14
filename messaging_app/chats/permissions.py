 from rest_framework import permissions
 from rest_framework.permissions import BasePermission, IsAuthenticated

 class IsOwner(permissions.BasePermission):

     def has_object_permission(self, request, view, obj):
         
         return obj.user == request.user

 class IsParticipantOfConversation(BasePermission):
    
     def has_permission(self, request, view):

         return request.user and request.user.is_authenticated

     def has_object_permission(self, request, view, obj):

         user = request.user

         if hasattr(obj, "conversation"):
             conversation = obj.conversation
         else:
             conversation = obj

         return conversation.participants.filter(id=user.id).exists()