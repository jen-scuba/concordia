# Generated by Django 3.2.22 on 2023-10-16 18:32

from django.db import migrations, models

import concordia.models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0084_rename_review_actions_sitereport_daily_review_actions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="storage_image",
            field=models.ImageField(
                max_length=255, upload_to=concordia.models.Asset.get_storage_path
            ),
        ),
    ]
