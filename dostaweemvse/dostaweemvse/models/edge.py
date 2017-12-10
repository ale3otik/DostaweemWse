from django.db import models


class Edge(models.Model):
    start_location_id = models.IntegerField()
    end_location_id = models.IntegerField()
    edge_type_id = models.IntegerField()
    length = models.IntegerField()


class TypeOfEdge(models.Model):
    cost = models.IntegerField()
    name = models.CharField(max_length=30)
