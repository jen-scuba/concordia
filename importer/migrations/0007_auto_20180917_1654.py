# Generated by Django 2.0.8 on 2018-09-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("importer", "0006_auto_20180912_0229")]

    operations = [
        migrations.AlterField(
            model_name="campaignitemassetcount",
            name="campaign_item_identifier",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="campaigntaskdetails",
            name="campaign_name",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="campaigntaskdetails",
            name="campaign_slug",
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name="campaigntaskdetails",
            name="project_name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="campaigntaskdetails",
            name="project_slug",
            field=models.SlugField(max_length=250),
        ),
    ]
