# Generated by Django 3.2.17 on 2023-02-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0063_banner_alert_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="alert_status",
            field=models.CharField(
                choices=[
                    ("DANGER", "Red"),
                    ("INFO", "Teal"),
                    ("PRIMARY", "Blue"),
                    ("SECONDA", "Grey"),
                    ("SUCCESS", "Green"),
                    ("WARN", "Yellow"),
                ],
                default="SUCCESS",
                max_length=7,
                verbose_name="Color",
            ),
        ),
    ]
