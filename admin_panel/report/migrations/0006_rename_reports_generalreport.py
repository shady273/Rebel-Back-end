# Generated by Django 5.0 on 2024-01-10 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_chevronphoto_alter_thanksphoto_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reports',
            new_name='GeneralReport',
        ),
    ]
