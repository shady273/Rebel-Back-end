import uuid
from django.db import models


class Merch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_uk = models.TextField()
    text_en = models.TextField()

    def __str__(self):
        return 'Merch'

    class Meta:
        verbose_name_plural = 'Merch'