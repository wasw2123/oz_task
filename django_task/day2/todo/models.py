from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '할 일'
        verbose_name_plural = '할 일 목록'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('cbv_todo_detail', kwargs={"pk": self.pk})


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField('메시지', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
