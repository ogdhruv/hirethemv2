# Generated by Django 4.0.8 on 2022-11-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_job_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-created']},
        ),
    ]
