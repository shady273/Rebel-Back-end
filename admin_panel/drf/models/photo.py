import uuid
from django.db import models

from drf.models.activity import OurActivity
from drf.models.donate import Donate
from drf.models.hero import Section
from drf.models.merch import Merch


class Photo(models.Model):
    section = models.ForeignKey(Section, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(OurActivity, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    donate = models.ForeignKey(Donate, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    merch = models.ForeignKey(Merch, related_name='photos', null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/photos')
