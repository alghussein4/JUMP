from django.db import models


class Governorate(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Hospital(models.Model):

    name = models.CharField(
        max_length=200
    )

    governorate = models.ForeignKey(
        Governorate,
        on_delete=models.CASCADE,
        related_name="hospitals"
    )

    address = models.TextField()

    latitude = models.FloatField()

    longitude = models.FloatField()

    def __str__(self):
        return self.name