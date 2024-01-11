import uuid
from django.db import models


class Reports(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title_uk = models.CharField()
    title_en = models.CharField()

    def __str__(self):
        return self.title_uk

    class Meta:
        verbose_name_plural = 'Загальний результат'


class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reports = models.ForeignKey(Reports, related_name='items', on_delete=models.CASCADE)
    title_uk = models.CharField()
    title_en = models.CharField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title_uk

