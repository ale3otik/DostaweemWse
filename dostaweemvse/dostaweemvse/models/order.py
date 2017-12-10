from django.db import models

class Order(models.model):
    route_id = models.ForeignKey(Route)
    metadata = models.CharField(max_length=50)
