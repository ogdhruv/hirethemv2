# Generated by Django 4.1.3 on 2022-11-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="room/photos"),
        ),
    ]