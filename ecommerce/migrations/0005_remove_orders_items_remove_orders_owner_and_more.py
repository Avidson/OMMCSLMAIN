# Generated by Django 4.2.3 on 2024-03-15 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_orders_ordered_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='owner',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]