# Generated by Django 5.0 on 2023-12-29 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0004_alter_photo_our_activity_alter_photo_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='our_activity',
            new_name='activity',
        ),
    ]
