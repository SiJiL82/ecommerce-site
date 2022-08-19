# Generated by Django 3.2 on 2022-08-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20220815_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='event',
            name='long',
        ),
        migrations.AddField(
            model_name='event',
            name='google_maps_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]