# Generated by Django 2.0.9 on 2018-12-04 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("concordia", "0020_auto_20181128_1718")]

    operations = [
        migrations.CreateModel(
            name="SiteReport",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("assets_total", models.IntegerField()),
                ("assets_published", models.IntegerField()),
                ("assets_not_started", models.IntegerField()),
                ("assets_in_progress", models.IntegerField()),
                ("assets_waiting_review", models.IntegerField()),
                ("assets_completed", models.IntegerField()),
                ("assets_unpublished", models.IntegerField()),
                ("items_published", models.IntegerField()),
                ("items_unpublished", models.IntegerField()),
                ("projects_published", models.IntegerField()),
                ("projects_unpublished", models.IntegerField()),
                ("anonymous_transcriptions", models.IntegerField()),
                ("transcriptions_saved", models.IntegerField()),
                ("distinct_tags", models.IntegerField()),
                ("tag_uses", models.IntegerField()),
                ("campaigns_published", models.IntegerField(blank=True, null=True)),
                ("campaigns_unpublished", models.IntegerField(blank=True, null=True)),
                ("users_registered", models.IntegerField(blank=True, null=True)),
                ("users_activated", models.IntegerField(blank=True, null=True)),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="concordia.Campaign",
                    ),
                ),
            ],
        )
    ]
