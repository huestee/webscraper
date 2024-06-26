# Generated by Django 5.0.6 on 2024-05-15 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reference', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_google_shopping', models.URLField()),
                ('id_casa_del_electrodomestico', models.CharField(max_length=50)),
                ('joined_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.product')),
            ],
        ),
    ]
