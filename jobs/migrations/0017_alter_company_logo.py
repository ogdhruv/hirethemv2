# Generated by Django 4.0.8 on 2022-11-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='../static/defaults/blogs/default.jpg', null=True, upload_to='jobs/companylogos'),
        ),
    ]