import uuid
from django.db import models


class ReportsPV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Фото відео звіт'


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reports = models.ForeignKey(ReportsPV, related_name='photo', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/photos')


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reports = models.ForeignKey(ReportsPV, related_name='video', on_delete=models.CASCADE)
    video_url = models.CharField()
