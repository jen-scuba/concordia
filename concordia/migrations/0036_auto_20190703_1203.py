# Generated by Django 2.2.2 on 2019-07-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("concordia", "0035_auto_20190627_1455")]

    operations = [
        migrations.AlterField(
            model_name="sitereport",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        )
    ]
