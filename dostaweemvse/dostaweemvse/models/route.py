from django.db import models


class Route(models.model):
    edges = models.ManyToManyField(Edge, through="Index")
    active_edge_index = models.IntegerField()

    def go_to_next_edge():
        active_edge_index += 1

    def get_active_edge_id():
        return edges.all()[active_edge_index]
