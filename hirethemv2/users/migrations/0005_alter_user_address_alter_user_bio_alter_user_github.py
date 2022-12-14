# Generated by Django 4.0.8 on 2022-11-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, help_text='Enter your address in format - your state, your country', max_length=500, null=True, verbose_name='Your State and Country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, help_text="\n\n             - Requires a unique link of your github profile.<br>\n             - Add link without 'https://'.\n\n            ", max_length=500, null=True, verbose_name='Github link'),
        ),
    ]
