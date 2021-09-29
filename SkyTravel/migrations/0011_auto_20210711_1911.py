# Generated by Django 3.2.5 on 2021-07-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SkyTravel', '0010_auto_20210711_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtrip',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SkyTravel.buschart'),
        ),
        migrations.AlterField(
            model_name='bustrip',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SkyTravel.buschart'),
        ),
    ]
