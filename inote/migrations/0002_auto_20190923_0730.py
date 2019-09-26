# Generated by Django 3.0a1 on 2019-09-22 22:30

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inote',
            name='date',
        ),
        migrations.AddField(
            model_name='inote',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 22, 30, 39, 961738, tzinfo=utc), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='inote',
            name='text',
            field=models.TextField(max_length=200, validators=[django.core.validators.MinLengthValidator(50)], verbose_name='text'),
        ),
    ]
