from .delivery_base import DeliveryBase
from .graph import Graph
from .order import Order
from .location import Location
from django.db import models


class Service(models.Model):
	def __init__(self):
		try:
			self.delivery_base = DeliveryBase.objects.get(pk=1)
		except:
			self.delivery_base = DeliveryBase()
			print('created new delivery_base object')

		self.delivery_base.save()

		super()

	@staticmethod
	def __fix_route_order(edge_container, from_location, to_location):
		location_dict = dict()

		for edge in edge_container:
			location_dict[edge.start_location.id] = edge

		right_order_route = []

		cur_location = from_location

		while cur_location != to_location:
			edge = location_dict[cur_location.id]
			right_order_route.append(edge)
			cur_location = edge.end_location

		return right_order_route

	def get_order_info(self, order_id):
		try:
			order = self.delivery_base.get_order(order_id)
		except Exception:
			return None

		order_info = {
			'source': order.from_location,
			'target': order.to_location,
			'route': Service.__fix_route_order(order.route.edges.all(),
				order.from_location, order.to_location),
			'position': order.route.active_edge_index,
			'weight': order.weight
		}

		return order_info

	def make_order(self, data):
		_from = Location.objects.filter(location_name=data['source'])[0]
		_to = Location.objects.filter(location_name=data['target'])[0]
		_route = None
		_weight = int(data['weight'])
		_max_cost = int(data['max_cost'])

		if 'meta' in data.keys():
			_metadata = data['meta']
		else:
			_metadata = ""

		_order = Order(
			route=_route,
			metadata=_metadata,
			from_location=_from,
			to_location=_to,
			max_cost=_max_cost,
			weight=_weight,
			)

		_route = Graph.build_route(_order)

		if _route:
			# _route.save()
			_order.route = _route
			_order.save()

			self.delivery_base.save_order(_order)
			self.delivery_base.save()
			return [True, _order.id]
		else:
			return [False,"unable to build graph"]
