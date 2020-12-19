# Users models definition
from django.db import models
from django.contrib.auth.models import User

class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Costumers(models.Model):
    first_name = models.CharField()
    middle_name = models.CharField()
    last_name = models.CharField()
    phone = models.CharField(max_length=10, blank=True, null=False, default='')
    email = models.EmailField()
