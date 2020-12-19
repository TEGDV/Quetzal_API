# Users views
# django imports
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# rest_framework imports
from rest_framework.parsers import JSONParser
# serializers
from users.serializers import UserListSerializer


def users_list(self, request):

    if request.method == 'GET':
        user_list = User.objects.all()
        serializer = UserListSerializer(user_list, many=True)
        return JsonResponse(serializer.data, safe=False)
