# Generated by Django 3.2 on 2022-07-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_alter_request_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]