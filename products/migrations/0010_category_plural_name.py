# Generated by Django 3.2 on 2022-08-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='plural_name',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
