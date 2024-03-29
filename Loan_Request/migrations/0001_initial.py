# Generated by Django 4.2.3 on 2023-12-16 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="loan_request_list",
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
                ("loan_amount", models.FloatField(default="0", editable=False)),
                ("loan_period", models.FloatField(default=6, editable=False)),
                ("interest_rate", models.FloatField(default=10, editable=False)),
                ("date_submitted", models.DateField(auto_now_add=True)),
                ("loan_approval", models.BooleanField(default=False)),
                ("account_name", models.CharField(default="None", max_length=200)),
                ("account_number", models.CharField(default="None", max_length=200)),
                ("bank_name", models.CharField(default="None", max_length=200)),
                ("purpose_for_loan", models.TextField(default="None")),
                ("loan_ref", models.CharField(default="None", max_length=500)),
                ("emi", models.FloatField(default="0", editable=False)),
                ("monthly_return", models.FloatField(default="0", editable=False)),
                ("loan_settled", models.BooleanField(default=False)),
                (
                    "client_name",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-date_submitted",),
                "index_together": {("id",)},
            },
        ),
    ]
