# Generated by Django 3.2.5 on 2021-07-11 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkyTravel', '0008_auto_20210711_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airtrip',
            name='arival',
        ),
        migrations.RemoveField(
            model_name='airtrip',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='airtrip',
            name='fromP',
        ),
        migrations.RemoveField(
            model_name='airtrip',
            name='returnDate',
        ),
        migrations.RemoveField(
            model_name='airtrip',
            name='toP',
        ),
        migrations.RemoveField(
            model_name='bustrip',
            name='arival',
        ),
        migrations.RemoveField(
            model_name='bustrip',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='bustrip',
            name='fromP',
        ),
        migrations.RemoveField(
            model_name='bustrip',
            name='returnDate',
        ),
        migrations.RemoveField(
            model_name='bustrip',
            name='toP',
        ),
    ]
