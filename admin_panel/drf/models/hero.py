import uuid
from django.db import models


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_uk = models.TextField()
    text_en = models.TextField()

    def __str__(self):
        return 'Hero'

    class Meta:
        verbose_name_plural = 'Hero'
