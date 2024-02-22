import uuid
from django.db import models
from report.models.reports import AllReports
from report.models import Items


class Reports(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_uk = models.TextField()
    text_en = models.TextField()

    def __str__(self):
        return 'Reports'

    class Meta:
        verbose_name_plural = 'Звіти'


class ReportsImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_reports = models.ForeignKey(Reports, related_name='photos', on_delete=models.CASCADE)
    report = models.ForeignKey(Items, related_name='report', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/photos')
