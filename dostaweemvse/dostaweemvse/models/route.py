from django.db import models
from .edge import Edge

class Route(models.Model):
    edges = models.ManyToManyField(Edge)
    active_edge_index = models.IntegerField()

    def go_to_next_edge(self):
        self.active_edge_index += 1
        self.save(update_fields=["active_edge_index"])

    def get_active_edge(self):
        return self.edges.all()[self.active_edge_index]
