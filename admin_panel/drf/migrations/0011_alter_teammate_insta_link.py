# Generated by Django 5.0 on 2023-12-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0010_auto_20231226_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammate',
            name='insta_link',
            field=models.CharField(),
        ),
    ]
