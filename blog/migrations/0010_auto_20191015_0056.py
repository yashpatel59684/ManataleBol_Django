# Generated by Django 2.2.5 on 2019-10-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191014_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='req',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='body',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
