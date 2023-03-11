from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from apps.core.serializers import SerializerBase

class UserSerializer(SerializerBase):
    count_permissions = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                'is_active', 'groups', 'count_permissions' 
            )
        
    def get_count_permissions(self, obj):
        return obj.user_permissions.count()
    
class GroupSerializer(SerializerBase):
    count_permissions = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ('id', 'name', 'count_permissions')

    def get_count_permissions(self, obj):
        return obj.permissions.count()
    
class PermissionSerializer(SerializerBase):
    count_users = serializers.SerializerMethodField()
    class Meta:
        model = Permission
        fields = ('id','name','group_set', 'count_users')

    def get_count_users(self, obj):
        return obj.user_set.count()