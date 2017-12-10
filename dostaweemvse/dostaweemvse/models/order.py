from django.db import models
from .route import Route
from .location import Location

class Order(models.model):
    route = models.ForeignKey(Route)
    metadata = models.CharField(max_length=50)
    from_location = models.ForeignKey(Location)
    to_location = models.ForeignKey(Location)
    max_cost = models.IntegerField()
