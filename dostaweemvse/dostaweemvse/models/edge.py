from django.db import models
from .location import Location

class TypeOfEdge(models.Model):
    cost = models.IntegerField()
    max_weight = models.IntegerField()
    name = models.CharField(max_length=30)
    
class Edge(models.Model):
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location1')
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location2')
    edge_type_id = models.ForeignKey(TypeOfEdge, on_delete=models.CASCADE)
    length = models.IntegerField()

    @property
    def cost(self):
        return self.edge_type_id.cost * self.length

