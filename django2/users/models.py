from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    profile_image = models.ImageField(upload_to='users/profile_images', default='users/blank_profile_image.png')
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    
    class Meta:
        verbose_name = '유저'
        verbose_name_plural = f'{verbose_name} 목록'
    
    def __str__(self):
        return self.nickname