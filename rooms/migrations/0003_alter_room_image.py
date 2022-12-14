# Generated by Django 4.1.3 on 2022-11-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="image",
            field=models.ImageField(
                blank=True,
                default="defaults/rooms/default.jpg",
                null=True,
                upload_to="room/photos",
            ),
        ),
    ]
