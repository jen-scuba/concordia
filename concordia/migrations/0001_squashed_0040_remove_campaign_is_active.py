# Generated by Django 2.0.9 on 2018-10-03 20:04

import django.contrib.postgres.fields.jsonb
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.get_or_create(name=settings.COMMUNITY_MANAGER_GROUP_NAME)
    Group.objects.get_or_create(name=settings.NEWSLETTER_GROUP_NAME)


class Migration(migrations.Migration):
    replaces = [
        ("concordia", "0001_initial"),
        ("concordia", "0002_auto_20180511_1722"),
        ("concordia", "0003_campaign_is_active"),
        ("concordia", "0004_auto_20180712_1857"),
        ("concordia", "0005_auto_20180713_1753"),
        ("concordia", "0006_auto_20180713_1759"),
        ("concordia", "0007_pageinuse"),
        ("concordia", "0008_auto_20180727_2021"),
        ("concordia", "0009_auto_20180730_2017"),
        ("concordia", "0010_auto_20180730_2032"),
        ("concordia", "0011_auto_20180730_2046"),
        ("concordia", "0007_campaign_s3_storage"),
        ("concordia", "0012_merge_20180806_1254"),
        ("concordia", "0013_auto_20180826_0928"),
        ("concordia", "0014_auto_20180904_1758"),
        ("concordia", "0015_auto_20180905_1756"),
        ("concordia", "0016_auto_20180906_1720"),
        ("concordia", "0017_auto_20180912_0229"),
        ("concordia", "0018_auto_20180917_1654"),
        ("concordia", "0019_auto_20180920_1503"),
        ("concordia", "0020_auto_20180922_0139"),
        ("concordia", "0021_auto_20180922_0202"),
        ("concordia", "0022_auto_20180924_1511"),
        ("concordia", "0023_auto_20180924_1511"),
        ("concordia", "0024_auto_20180924_1529"),
        ("concordia", "0025_auto_20180924_2022"),
        ("concordia", "0026_auto_20180925_2000"),
        ("concordia", "0027_auto_20180926_1705"),
        ("concordia", "0026_creategroups"),
        ("concordia", "0028_merge_20180927_1529"),
        ("concordia", "0029_remove_userprofile_myfile"),
        ("concordia", "0029_auto_20180928_1437"),
        ("concordia", "0030_merge_20181002_1350"),
        ("concordia", "0031_auto_20181002_1900"),
        ("concordia", "0032_auto_20181002_1901"),
        ("concordia", "0033_auto_20181002_1909"),
        ("concordia", "0034_remove_transcription_parent"),
        ("concordia", "0035_auto_20181002_1914"),
        ("concordia", "0036_remove_item_slug"),
        ("concordia", "0037_auto_20181002_1939"),
        ("concordia", "0030_merge_20180928_1740"),
        ("concordia", "0031_merge_20181002_1846"),
        ("concordia", "0038_merge_20181002_1949"),
        ("concordia", "0039_remove_campaign_s3_storage"),
        ("concordia", "0040_remove_campaign_is_active"),
    ]

    initial = True

    dependencies = [
        ("auth", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Asset",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("media_url", models.URLField(max_length=255)),
                (
                    "media_type",
                    models.CharField(
                        choices=[("IMG", "Image"), ("AUD", "Audio"), ("VID", "Video")],
                        db_index=True,
                        max_length=4,
                    ),
                ),
                ("sequence", models.PositiveIntegerField(default=1)),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "0%"),
                            ("25", "25%"),
                            ("50", "50%"),
                            ("75", "75%"),
                            ("100", "100%"),
                            ("DONE", "Complete"),
                        ],
                        default="0",
                        max_length=4,
                    ),
                ),
            ],
            options={"ordering": ["title", "sequence"]},
        ),
        migrations.CreateModel(
            name="Campaign",
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
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField(blank=True)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "0%"),
                            ("25", "25%"),
                            ("50", "50%"),
                            ("75", "75%"),
                            ("100", "100%"),
                            ("DONE", "Complete"),
                        ],
                        default="0",
                        max_length=4,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                ("category", models.CharField(blank=True, max_length=12)),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Edit", "Open for Edit"),
                            ("Submitted", "Submitted for Review"),
                            ("Completed", "Transcription Completed"),
                            ("Inactive", "Inactive"),
                            ("Active", "Active"),
                        ],
                        default="Edit",
                        max_length=10,
                    ),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Campaign",
                    ),
                ),
                ("is_publish", models.BooleanField(default=False)),
            ],
            options={"ordering": ["title"]},
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("value", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Transcription",
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
                ("user_id", models.PositiveIntegerField(db_index=True)),
                ("text", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Edit", "Open for Edit"),
                            ("Submitted", "Submitted for Review"),
                            ("Completed", "Transcription Completed"),
                            ("Inactive", "Inactive"),
                            ("Active", "Active"),
                        ],
                        default="Edit",
                        max_length=10,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Asset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAssetTagCollection",
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
                ("user_id", models.PositiveIntegerField(db_index=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Asset",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="concordia.Tag")),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="project", unique_together={("slug", "campaign")}
        ),
        migrations.AlterField(
            model_name="asset",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                ],
                default="Edit",
                max_length=4,
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                ],
                default="Edit",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                    ("Inactive", "Inactive"),
                    ("Active", "Active"),
                ],
                default="Edit",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                ],
                default="Edit",
                max_length=4,
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                ],
                default="Edit",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="PageInUse",
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
                ("page_url", models.CharField(max_length=256)),
                ("created_on", models.DateTimeField(editable=False)),
                ("updated_on", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="campaign",
            name="is_publish",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="status",
            field=models.CharField(
                choices=[
                    ("Edit", "Open for Edit"),
                    ("Submitted", "Submitted for Review"),
                    ("Completed", "Transcription Completed"),
                    ("Inactive", "Inactive"),
                    ("Active", "Active"),
                ],
                default="Edit",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Item",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("item_url", models.URLField(max_length=255)),
                ("item_id", models.CharField(blank=True, max_length=100)),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    "thumbnail_url",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Edit", "Open for Edit"),
                            ("Submitted", "Submitted for Review"),
                            ("Completed", "Transcription Completed"),
                            ("Inactive", "Inactive"),
                            ("Active", "Active"),
                        ],
                        default="Edit",
                        max_length=10,
                    ),
                ),
                ("is_publish", models.BooleanField(default=False)),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Project",
                    ),
                ),
            ],
            options={"ordering": ["item_id"]},
        ),
        migrations.AlterModelOptions(
            name="asset", options={"ordering": ["item", "sequence"]}
        ),
        migrations.AddField(
            model_name="asset",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="concordia.Item",
            ),
        ),
        migrations.AlterModelOptions(
            name="asset", options={"ordering": ["title", "sequence"]}
        ),
        migrations.AddField(
            model_name="asset",
            name="download_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="resource_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="slug",
            field=models.SlugField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name="campaign", name="title", field=models.CharField(max_length=500)
        ),
        migrations.AlterField(
            model_name="project", name="slug", field=models.SlugField(max_length=500)
        ),
        migrations.AlterField(
            model_name="project", name="title", field=models.CharField(max_length=500)
        ),
        migrations.AlterField(
            model_name="campaign",
            name="slug",
            field=models.SlugField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name="campaign", name="title", field=models.CharField(max_length=80)
        ),
        migrations.AlterField(
            model_name="project", name="slug", field=models.SlugField(max_length=80)
        ),
        migrations.AlterField(
            model_name="project", name="title", field=models.CharField(max_length=80)
        ),
        migrations.AlterField(
            model_name="asset",
            name="metadata",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, null=True
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="metadata",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, null=True
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="metadata",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, null=True
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="media_url",
            field=models.TextField(
                max_length=255, verbose_name="Path component of the URL"
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="concordia.Item"
            ),
        ),
        migrations.AlterField(
            model_name="item", name="title", field=models.CharField(max_length=300)
        ),
        migrations.AlterField(
            model_name="item",
            name="metadata",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                help_text="Raw metadata returned by the remote API",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="tag", name="value", field=models.CharField(max_length=50)
        ),
        migrations.RenameField(
            model_name="campaign", old_name="is_publish", new_name="published"
        ),
        migrations.RenameField(
            model_name="item", old_name="is_publish", new_name="published"
        ),
        migrations.RenameField(
            model_name="project", old_name="is_publish", new_name="published"
        ),
        migrations.RunPython(code=create_groups),
        migrations.AlterField(
            model_name="tag",
            name="value",
            field=models.CharField(
                max_length=50,
                validators=[django.core.validators.RegexValidator("^[- _'\\w]{1,50}$")],
            ),
        ),
        migrations.RenameField(
            model_name="transcription", old_name="user_id", new_name="user"
        ),
        migrations.RenameField(
            model_name="userassettagcollection", old_name="user_id", new_name="user"
        ),
        migrations.AlterField(
            model_name="transcription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="userassettagcollection",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="pageinuse",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="item", unique_together={("item_id", "project")}
        ),
        migrations.AlterUniqueTogether(
            name="asset", unique_together={("slug", "item")}
        ),
        migrations.AlterModelOptions(name="item", options={}),
        migrations.AlterField(
            model_name="item",
            name="item_id",
            field=models.CharField(
                help_text="Unique item ID assigned by the upstream source",
                max_length=100,
            ),
        ),
    ]
