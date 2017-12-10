from django.core.management.base import BaseCommand

from dostaweemvse.models.location import *
from dostaweemvse.models.edge import *


class Command(BaseCommand):

    def _initialize(self):
        locations = [Location(location_name='Колумбия'),
                     Location(location_name='Москва'),
                     Location(location_name='Мексика'),
                     Location(location_name='Лобня')]
        loc_ids = []
        for loc in locations:
            loc.save()
            loc_ids.append(loc.id)
        type_ids = []
        types = [TypeOfEdge(cost=50, max_weight=10, name='Багаж'),
                 TypeOfEdge(cost=500, max_weight=1000, name='Контейнер'),
                 TypeOfEdge(cost=1, max_weight=20, name='Элка')
                 ]
        for type_ in types:
            type_.save()
            type_ids.append(type_.id)
        edges = [Edge(start_location=locations[2], end_location=locations[1], edge_type_id=types[1] ,length=8000),
                 Edge(start_location=locations[0], end_location=locations[2], edge_type_id=types[1] ,length=1000),
                 Edge(start_location=locations[0], end_location=locations[3], edge_type_id=types[0] ,length=8000),
                 Edge(start_location=locations[1], end_location=locations[3], edge_type_id=types[2] ,length=10)
                 ]
        for edge in edges:
            edge.save()

    def handle(self, *args, **options):
        self._initialize()
