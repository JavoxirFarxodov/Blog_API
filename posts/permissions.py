from rest_framework import permissions

class IsAuthorOrReandOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina korish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        #O'zgartirish ya'ni yozi uchun rxsatnoma faqatgina post muallifigagina beriladi
        return obj.author ==request.user