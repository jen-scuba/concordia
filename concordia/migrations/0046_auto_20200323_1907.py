# Generated by Django 2.2.11 on 2020-03-23 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0045_auto_20200323_1832"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="transcription_status",
            field=models.CharField(
                choices=[
                    ("not_started", "Not Started"),
                    ("in_progress", "In Progress"),
                    ("submitted", "Needs Review"),
                    ("completed", "Completed"),
                ],
                db_index=True,
                default="not_started",
                editable=False,
                max_length=20,
            ),
        ),
    ]
