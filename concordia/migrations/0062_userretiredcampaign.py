# Generated by Django 3.2.14 on 2023-01-20 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("concordia", "0061_sitereport_registered_contributors"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRetiredCampaign",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("asset_count", models.IntegerField(blank=True, null=True)),
                ("asset_tag_count", models.IntegerField(blank=True, null=True)),
                (
                    "transcribe_count",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="transcription save/submit count",
                    ),
                ),
                (
                    "review_count",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="transcription review count"
                    ),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.campaign",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
