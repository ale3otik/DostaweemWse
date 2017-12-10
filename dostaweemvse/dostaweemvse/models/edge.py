from django.db import models


class Edge(models.Model):
    start_location = models.IntegerField()
    end_location = models.IntegerField()
    edge_type_id = models.IntegerField()
    length = models.IntegerField()


class TypeOfEdge(models.Model):
    edge_type_id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()
    name = models.CharField(max_length=30)
