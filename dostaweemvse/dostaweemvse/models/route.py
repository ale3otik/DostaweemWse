from django.db import models


class Route(models.model):
    edges = models.ManyToManyField(Edge, through="Index")
    active_edge_index = models.IntegerField()

    def go_to_next_edge(self):
        self.active_edge_index += 1
        self.save(update_fields=["active_edge_index"])

    def get_active_edge_id(self):
        return self.edges.all()[self.active_edge_index]
