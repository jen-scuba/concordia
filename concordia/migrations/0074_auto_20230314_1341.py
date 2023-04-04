# Generated by Django 3.2.18 on 2023-03-14 13:41

from django.db import migrations


def forwards_func(apps, schema_editor):
    # moved all of this functionality to tasks.py
    # leaving this migration here, just in case any environments still reference it
    pass


def reverse_func(apps, schema_editor):
    # reverse_func() should delete instances.
    UserProfileActivity = apps.get_model("concordia", "UserProfileActivity")
    db_alias = schema_editor.connection.alias
    UserProfileActivity.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0073_auto_20230314_1327"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]