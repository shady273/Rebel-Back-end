# Generated by Django 5.0 on 2024-01-10 08:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThanksPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/photos')),
            ],
        ),
    ]
