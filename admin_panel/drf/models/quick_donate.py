import uuid
from django.db import models


class QuickDonate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donate_link = models.CharField()

    def __str__(self):
        return 'Швидкий донат'

    class Meta:
        verbose_name_plural = 'Швидкий донат'