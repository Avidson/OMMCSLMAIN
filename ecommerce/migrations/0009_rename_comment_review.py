# Generated by Django 4.2.3 on 2024-03-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_comment_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
    ]