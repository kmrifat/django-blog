from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model."""
    email = models.EmailField('Email Address', unique=True)

    class Meta:
        db_table = 'auth_user'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
