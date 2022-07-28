# Generated by Django 3.2 on 2022-07-28 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('size', models.CharField(choices=[('6-9m', '6-9 months'), ('9-12m', '9-12 months'), ('12-18m', '12-18 months'), ('18-24m', '18-24 months'), ('2-3y', '2-3 years'), ('3-4y', '3-4 years'), ('4-5y', '4-5 years'), ('5-6y', '5-6 years'), ('6-7y', '6-7 years'), ('7-8y', '7-8 years'), ('8-9y', '8-9 years'), ('9-10y', '9-10 years')], max_length=254)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]