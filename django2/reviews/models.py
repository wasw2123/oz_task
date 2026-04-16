from django.db import models

from django.conf import settings
from config.models import BaseModel
from restaurants.models import Restaurant


User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    comment = models.TextField()


    class Meta:
        verbose_name = '리뷰'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.title