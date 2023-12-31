# Generated by Django 2.0.9 on 2018-11-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("concordia", "0017_change_transcription_supersedes_related_name")]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="display_on_homepage",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="ordering",
            field=models.IntegerField(
                default=0,
                help_text="Sort order override: higher values will be listed first",
            ),
        ),
    ]
