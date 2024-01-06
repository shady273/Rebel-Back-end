# Generated by Django 5.0 on 2024-01-05 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0012_reports_reportsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsimage',
            name='image_reports',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='drf.reports'),
        ),
    ]