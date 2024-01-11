import uuid
from django.db import models


class ThanksPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/photos')

    class Meta:
        verbose_name_plural = 'Подяки'
