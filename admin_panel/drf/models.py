from django.db import models


class Teammate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False)
    role = models.CharField(null=False)
    insta_link = models.CharField(null=False)
    image_data = models.ImageField(upload_to='images/teammate_avatar', null=False)

    def __str__(self):
        return self.name
