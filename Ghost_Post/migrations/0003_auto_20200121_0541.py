# Generated by Django 3.0.2 on 2020-01-21 05:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ghost_Post', '0002_auto_20200121_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='secretKey',
            field=models.CharField(default='666666', max_length=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 21, 5, 41, 5, 21154, tzinfo=utc), verbose_name='date published'),
        ),
    ]
