# Generated by Django 3.2.5 on 2021-07-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkyTravel', '0002_auto_20210711_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtrip',
            name='baby',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bustrip',
            name='baby',
            field=models.BigIntegerField(),
        ),
    ]
