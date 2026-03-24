from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from utils.time_stamp_model import TimeStampModel

User = AUTH_USER_MODEL

# Create your models here.
class Todo(TimeStampModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    class Meta:
        verbose_name = '할 일'
        verbose_name_plural = '할 일 목록'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('cbv_todo_detail', kwargs={"pk": self.pk})


class Comment(TimeStampModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField('메시지', max_length=200)
