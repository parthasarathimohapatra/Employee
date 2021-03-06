# Generated by Django 3.0.3 on 2020-05-25 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0002_auto_20200525_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='star_time',
        ),
        migrations.AddField(
            model_name='employee',
            name='start_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Conversation Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='end_time',
            field=models.TimeField(auto_now_add=True, verbose_name='Conversation Time'),
        ),
    ]
