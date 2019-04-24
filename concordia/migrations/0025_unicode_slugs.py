# Generated by Django 2.2 on 2019-04-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0024_add_site_report_ordering")]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="slug",
            field=models.SlugField(allow_unicode=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="slug",
            field=models.SlugField(allow_unicode=True, max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(allow_unicode=True, max_length=80),
        ),
    ]