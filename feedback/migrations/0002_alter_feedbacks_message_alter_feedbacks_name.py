# Generated by Django 4.2.3 on 2024-02-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='message',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='name',
            field=models.CharField(editable=False, max_length=300),
        ),
    ]
