# Generated by Django 2.2.11 on 2020-03-23 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0044_auto_20200323_1827"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="asset",
            index=models.Index(
                fields=["published", "transcription_status"],
                name="concordia_a_publish_4761f1_idx",
            ),
        ),
    ]
