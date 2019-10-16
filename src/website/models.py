from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model."""
    email = models.EmailField('Email Address', unique=True)

    class Meta:
        db_table = 'auth_user'


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
