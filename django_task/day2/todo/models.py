from io import BytesIO
from pathlib import Path

from django.conf.global_settings import AUTH_USER_MODEL
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

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
    completed_image = models.ImageField(null=True, blank=True, upload_to='todo/%Y-%m-%d/')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='todo/%Y-%m-%d/thumbnail')

    class Meta:
        verbose_name = '할 일'
        verbose_name_plural = '할 일 목록'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.completed_image:
            return super().save(*args, **kwargs)

        image = Image.open(self.completed_image)
        image.thumbnail((384, 216))

        image_path = Path(self.completed_image.name)
        thumbnail_name = image_path.stem
        thumbnail_extension = image_path.suffix.lower()
        thumbnail_filename = f"{thumbnail_name}_thumbnail{thumbnail_extension}"

        if thumbnail_extension in ['.jpg', '.jpeg']:
            file_type = 'JPEG'
        elif thumbnail_extension == '.png':
            file_type = "PNG"
        elif thumbnail_extension == '.gif':
            file_type = "GIF"
        else:
            return super().save(*args, **kwargs)

        temp_thumb = BytesIO()
        image.save(temp_thumb, file_type)
        temp_thumb.seek(0)

        self.thumbnail.save(thumbnail_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return super().save(*args, **kwargs)






    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('cbv_todo_detail', kwargs={"pk": self.pk})


class Comment(TimeStampModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField('메시지', max_length=200)
