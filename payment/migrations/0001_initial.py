# Generated by Django 4.2.3 on 2023-12-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(editable=False, max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("amount", models.FloatField(default="0", editable=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("paid", models.BooleanField(default=False)),
                ("payment_purpose", models.CharField(max_length=200)),
                ("paystack_ref", models.CharField(blank=True, max_length=15)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]
