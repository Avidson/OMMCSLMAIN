# Generated by Django 4.2.3 on 2024-02-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monthly_due', '0006_april_payment_ref_august_payment_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='july',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
