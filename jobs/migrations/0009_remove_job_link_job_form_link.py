# Generated by Django 4.0.8 on 2022-11-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_job_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='link',
        ),
        migrations.AddField(
            model_name='job',
            name='form_link',
            field=models.CharField(blank=True, default='', help_text='Your google form link', max_length=100, null=True),
        ),
    ]
