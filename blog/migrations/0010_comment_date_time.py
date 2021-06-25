# Generated by Django 3.2.2 on 2021-06-06 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210606_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]