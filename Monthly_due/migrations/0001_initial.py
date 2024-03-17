# Generated by Django 4.2.3 on 2023-12-16 12:23

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
            name="September",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="October",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="November",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="May",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="march",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="June",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="July",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="january",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="february",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="December",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="August",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="April",
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
                ("paid", models.BooleanField(default=False)),
                ("date_paid", models.DateField(editable=False)),
                (
                    "remark",
                    models.CharField(
                        default="Your payment is upto date!", max_length=200
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]