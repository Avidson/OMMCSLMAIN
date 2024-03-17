# Generated by Django 4.2.3 on 2023-12-16 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dashboard",
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
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "profile_owner",
                    models.OneToOneField(
                        default=0,
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        default="your occupation", editable=False, max_length=150
                    ),
                ),
                (
                    "state_residence",
                    models.CharField(
                        default="Home address", editable=False, max_length=200
                    ),
                ),
                (
                    "home_address",
                    models.CharField(default="address", editable=False, max_length=200),
                ),
                (
                    "phone_number",
                    models.CharField(
                        default="0908987679", editable=False, max_length=200
                    ),
                ),
                (
                    "email",
                    models.CharField(default="example@email.com", max_length=200),
                ),
                ("registration_fee", models.FloatField(default=0, editable=False)),
                ("payment_date", models.DateField(auto_now=True)),
                ("paid", models.BooleanField(default=False)),
                (
                    "payment_ref",
                    models.CharField(default="None", editable=False, max_length=200),
                ),
                ("passport", models.ImageField(default="None", upload_to="")),
            ],
        ),
    ]