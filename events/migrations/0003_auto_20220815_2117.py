# Generated by Django 3.2 on 2022-08-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20220815_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='long',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
