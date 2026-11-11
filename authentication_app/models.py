from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    USER_TYPES = [('Instructor','Instructor'),('Student','Student')]
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatar_img/', blank=True)
    bio = models.TextField(blank=True)
    user_type = models.CharField(choices=USER_TYPES, max_length=10, default='Student')

    def __str__(self):
        return f'{self.user_type} - {self.email}'