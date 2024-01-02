import uuid
from django.db import models

from drf.models.activity import OurActivity
from drf.models.hero import Section


class Photo(models.Model):
    section = models.ForeignKey(Section, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(OurActivity, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/photos')
