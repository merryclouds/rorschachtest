# Generated by Django 4.2.4 on 2024-02-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_consent_alter_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='consent',
            field=models.BooleanField(default=False),
        ),
    ]