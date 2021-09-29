from django.db import models
from django.contrib.auth.models import User
import uuid

class Places(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class AirChart(models.Model):
    fromP = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="fromPA")
    toP = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="toPA")
    departure = models.TimeField(max_length=120)
    arival = models.TimeField(max_length=120)
    adultcost = models.FloatField()
    childcost = models.FloatField()

    def __str__(self):
        return (self.fromP.name + " - " + self.toP.name)


class BusChart(models.Model):
    fromP = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="fromPB")
    toP = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="toPB")
    departure = models.TimeField()
    arival = models.TimeField()
    adultcost = models.FloatField()
    childcost = models.FloatField()

    def __str__(self):
        return (self.fromP.name + " - " + self.toP.name)

class BusTrip(models.Model):
    ticket = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(BusChart, on_delete=models.CASCADE)
    adult = models.BigIntegerField()
    child = models.BigIntegerField()
    baby = models.BigIntegerField()
    totalcost = models.FloatField()
    departureDate = models.DateField()
    payment = models.CharField(max_length=120)

    def __str__(self):
        return str(self.ticket) + " - " + self.payment
    

class AirTrip(models.Model):
    ticket = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(AirChart, on_delete=models.CASCADE)
    adult = models.BigIntegerField()
    child = models.BigIntegerField()
    baby = models.BigIntegerField()
    totalcost = models.FloatField()
    departureDate = models.DateField()
    payment = models.CharField(max_length=120)

    def __str__(self):
        return str(self.ticket) + " - " + self.payment

