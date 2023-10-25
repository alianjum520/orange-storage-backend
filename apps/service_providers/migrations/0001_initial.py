# Generated by Django 4.2 on 2023-09-18 09:51

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("country_code", models.CharField(blank=True, max_length=3, null=True)),
                ("county", models.CharField(blank=True, max_length=255, null=True)),
                ("postcode", models.IntegerField(blank=True, null=True)),
                ("district", models.CharField(blank=True, max_length=255, null=True)),
                ("lat", models.FloatField(blank=True, null=True)),
                ("lon", models.FloatField(blank=True, null=True)),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movers",
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
                ("name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("fax_number", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.CharField(blank=True, max_length=250, null=True)),
                ("facebook", models.CharField(blank=True, max_length=250, null=True)),
                ("instagram", models.CharField(blank=True, max_length=250, null=True)),
                ("twitter", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "google_buisness",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("working_hours", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organizers",
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
                ("name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("fax_number", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.CharField(blank=True, max_length=250, null=True)),
                ("facebook", models.CharField(blank=True, max_length=250, null=True)),
                ("instagram", models.CharField(blank=True, max_length=250, null=True)),
                ("twitter", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "google_buisness",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "unit_numbers",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(111111),
                        ]
                    ),
                ),
                ("size", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StorageUnitProvider",
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
                ("name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("fax_number", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.CharField(blank=True, max_length=250, null=True)),
                ("facebook", models.CharField(blank=True, max_length=250, null=True)),
                ("instagram", models.CharField(blank=True, max_length=250, null=True)),
                ("twitter", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "google_buisness",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
