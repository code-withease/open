from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# import uuid


class BaseUser(AbstractUser):
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)

    REQUIRED_FIELDS = ['']


    class Meta:
        abstract = True