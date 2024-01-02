import uuid
from django.db import models


class OurActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return 'Our activity'

    class Meta:
        verbose_name_plural = 'Наша діяльність'


class TextActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_activity = models.ForeignKey(OurActivity, related_name='text', on_delete=models.CASCADE)
    text_uk = models.TextField()
    text_en = models.TextField()
