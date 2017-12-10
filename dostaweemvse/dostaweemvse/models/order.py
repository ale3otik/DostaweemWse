from django.db import models
from .route import Route
from .location import Location

class Order(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    metadata = models.CharField(max_length=50)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    max_cost = models.IntegerField()
    weight = models.IntegerField()
