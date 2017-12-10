from django.db import models


class Location(models.model):
    location_name = models.CharField(max_length=30)
