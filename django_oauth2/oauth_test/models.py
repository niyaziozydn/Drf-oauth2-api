from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(
        max_length=256
    )

class City(models.Model):
    name = models.CharField(
        max_length=256
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )

class Address(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE

    )
    address = models.CharField(
        max_length=256
    )
    name = models.CharField(
        max_length=256
    )