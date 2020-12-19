from django.urls import path
from users.views import UsersList as user_views

urlspatterns = [
    path('users/', user_views.as_view()),
]
