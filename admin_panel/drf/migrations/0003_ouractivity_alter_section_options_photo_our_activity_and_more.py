# Generated by Django 5.0 on 2023-12-29 17:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_alter_section_options_alter_teammate_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text_1_uk', models.TextField()),
                ('text_2_uk', models.TextField()),
                ('text_3_uk', models.TextField()),
                ('text_1_en', models.TextField()),
                ('text_2_en', models.TextField()),
                ('text_3_en', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Our activity',
            },
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': 'Hero'},
        ),
        migrations.AddField(
            model_name='photo',
            name='our_activity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='drf.section'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='drf.ouractivity'),
        ),
    ]
