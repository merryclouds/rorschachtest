# Generated by Django 4.2.4 on 2023-11-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0003_alter_responsecode_loc_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structuralsummary',
            name='left_eb',
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='GHR_PHR',
            field=models.CharField(default='', max_length=20, verbose_name='GHR:PHR'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='a_p',
            field=models.CharField(default='', max_length=20, verbose_name='a:p'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='afr',
            field=models.FloatField(default=0.0, verbose_name='affection ratio'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='blends_r',
            field=models.CharField(default='', max_length=20, verbose_name='Blends:R'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='ca_c_prop',
            field=models.CharField(default='', max_length=20, verbose_name="SumC':WsumC"),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='f_c_prop',
            field=models.CharField(default='', max_length=20, verbose_name='FC:CF+C'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='pure_c',
            field=models.IntegerField(default=0, verbose_name='pure C'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_Ca',
            field=models.PositiveIntegerField(default=0, verbose_name="sum_C'"),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_FM',
            field=models.PositiveIntegerField(default=0, verbose_name='sumFM'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_T',
            field=models.PositiveIntegerField(default=0, verbose_name='sum_T'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_V',
            field=models.PositiveIntegerField(default=0, verbose_name='sum_V'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_Y',
            field=models.PositiveIntegerField(default=0, verbose_name='sum_Y'),
        ),
        migrations.AddField(
            model_name='structuralsummary',
            name='sum_m',
            field=models.PositiveIntegerField(default=0, verbose_name='sum_m'),
        ),
    ]
