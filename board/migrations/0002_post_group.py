# Generated by Django 4.2.4 on 2023-11-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate')], default='beginner', max_length=20),
        ),
    ]
