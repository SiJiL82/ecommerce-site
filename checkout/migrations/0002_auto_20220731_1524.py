# Generated by Django 3.2 on 2022-07-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='United Kingdom', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]