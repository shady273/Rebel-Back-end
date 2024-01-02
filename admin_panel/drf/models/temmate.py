import uuid
from django.db import models


class Teammate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_uk = models.CharField(max_length=255, null=False)
    name_en = models.CharField(max_length=255, null=False)
    role_uk = models.CharField(max_length=255, null=False)
    role_en = models.CharField(max_length=255, null=False)
    insta_link = models.CharField(max_length=255, blank=True, null=True)
    image_data = models.ImageField(upload_to='images/teammate_avatar', )

    def __str__(self):
        return self.name_uk

    class Meta:
        verbose_name_plural = 'Команда'
