# Generated by Django 2.0.8 on 2018-09-24 13:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("importer", "0012_auto_20180923_0231")]

    operations = [
        migrations.RenameField(
            model_name="importjob", old_name="source_url", new_name="url"
        )
    ]
