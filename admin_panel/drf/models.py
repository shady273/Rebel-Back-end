from django.db import models


class Teammate(models.Model):
    id = models.AutoField(primary_key=True)
    name_uk = models.CharField(null=False)
    name_en = models.CharField(null=False)
    role_uk = models.CharField(null=False)
    role_en = models.CharField(null=False)
    insta_link = models.CharField(blank=True, null=True)
    image_data = models.ImageField(upload_to='images/teammate_avatar', null=False)

    def __str__(self):
        return self.name_uk
