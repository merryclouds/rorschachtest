# Generated by Django 4.2.10 on 2024-02-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file'),
        ),
    ]
