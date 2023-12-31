# Generated by Django 2.1.5 on 2019-01-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("concordia", "0022_auto_20181211_1310")]

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
                default="not_started",
                editable=False,
                max_length=20,
            ),
        )
    ]
