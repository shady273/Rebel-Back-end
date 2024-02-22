# Generated by Django 5.0 on 2024-01-16 20:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChevronPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/photos')),
            ],
            options={
                'verbose_name_plural': 'Шеврони',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title_uk', models.CharField()),
                ('title_en', models.CharField()),
                ('text_uk', models.TextField()),
                ('text_en', models.TextField()),
                ('news_url', models.CharField()),
                ('image', models.ImageField(upload_to='images/photos')),
            ],
            options={
                'verbose_name_plural': 'Про нас говорять',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title_uk', models.CharField()),
                ('title_en', models.CharField()),
            ],
            options={
                'verbose_name_plural': 'Загальний результат',
            },
        ),
        migrations.CreateModel(
            name='ReportsPV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Фото відео звіт',
            },
        ),
        migrations.CreateModel(
            name='ThanksPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/photos')),
            ],
            options={
                'verbose_name_plural': 'Подяки',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title_uk', models.CharField()),
                ('title_en', models.CharField()),
                ('quantity', models.IntegerField()),
                ('reports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='report.reports')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/photos')),
                ('reports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='report.reportspv')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video_url', models.CharField()),
                ('reports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='report.reportspv')),
            ],
        ),
    ]