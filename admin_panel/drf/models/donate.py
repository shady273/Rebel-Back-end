import uuid
from django.db import models


class Donate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_uk = models.TextField()
    text_en = models.TextField()
    goal_uk = models.CharField()
    goal_en = models.CharField()
    donata_link = models.CharField()

    def __str__(self):
        return 'Терміновий збір'

    class Meta:
        verbose_name_plural = 'Терміновий збір'
