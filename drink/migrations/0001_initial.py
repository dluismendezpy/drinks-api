# Generated by Django 4.1.5 on 2023-01-17 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drink",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                (
                    "is_available",
                    models.BooleanField(
                        default=True,
                        help_text="Handle drink available in stock",
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
    ]