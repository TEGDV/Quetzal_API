from rest_framework import serializers
from django.contrib.auth.models import User

class UserListSerializer(serializers.ModelSerializer):
    class META:
        model = User
        fields = ['id','email','username']
