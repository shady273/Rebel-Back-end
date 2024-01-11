import uuid
from django.db import models


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title_uk = models.CharField()
    title_en = models.CharField()
    text_uk = models.TextField()
    text_en = models.TextField()
    news_url = models.CharField()
    image = models.ImageField(upload_to='images/photos')

    def __str__(self):
        return self.title_uk

    class Meta:
        verbose_name_plural = 'Про нас говорять'