from django.db import models
from .location import Location

class Edge(models.Model):
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    edge_type_id = models.ForeignKey(TypeOfEdge, on_delete=models.CASCADE)
    length = models.IntegerField()


class TypeOfEdge(models.Model):
    cost = models.IntegerField()
    max_weight = models.IntegerField()
    name = models.CharField(max_length=30)
