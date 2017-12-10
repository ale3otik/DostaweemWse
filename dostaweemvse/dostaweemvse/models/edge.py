from django.db import models


class Edge(models.Model):
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    edge_type_id = models.ForeignKey(TypeOfEdge, on_delete=models.CASCADE)


class TypeOfEdge(models.Model):
    edge_type_id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()
    max_weight = models.IntegerField()
    name = models.CharField(max_length=30)
