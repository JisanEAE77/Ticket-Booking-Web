# Generated by Django 3.2.5 on 2021-07-11 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SkyTravel', '0012_auto_20210711_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('adult', models.BigIntegerField()),
                ('child', models.BigIntegerField()),
                ('baby', models.BigIntegerField()),
                ('totalcost', models.FloatField()),
                ('departureDate', models.DateField()),
                ('payment', models.CharField(max_length=120)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SkyTravel.buschart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AirTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('adult', models.BigIntegerField()),
                ('child', models.BigIntegerField()),
                ('baby', models.BigIntegerField()),
                ('totalcost', models.FloatField()),
                ('departureDate', models.DateField()),
                ('payment', models.CharField(max_length=120)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SkyTravel.buschart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
