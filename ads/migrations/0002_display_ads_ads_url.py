# Generated by Django 4.2.3 on 2024-02-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='display_ads',
            name='ads_url',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
