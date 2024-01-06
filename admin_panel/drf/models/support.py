import uuid
from django.db import models


class Support(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_uk = models.CharField(max_length=255, null=False)
    name_en = models.CharField(max_length=255, null=False)
    link = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='images/support_logo', )

    def __str__(self):
        return self.name_uk

    class Meta:
        verbose_name_plural = 'Нас підтримують'
