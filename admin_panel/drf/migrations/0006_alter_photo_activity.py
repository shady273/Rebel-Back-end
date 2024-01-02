# Generated by Django 5.0 on 2023-12-29 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0005_rename_our_activity_photo_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='activity',
            field=models.ForeignKey(blank=True, limit_choices_to={'section': None}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='drf.ouractivity'),
        ),
    ]
