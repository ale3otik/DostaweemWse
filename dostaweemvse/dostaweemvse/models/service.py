from .delivery_base import DeliveryBase
from .graph import Graph
from .order import Order
from .location import Location


class Service(object):
	def __init__(self):
		self.delivery_base = DeliveryBase()
		self.delivery_base.save()

	def get_order_info(self, order_id):
		try:
			order = self.delivery_base.get_order(order_id)
		except Exception:
			return None

		order_info = {
			'source': order.from_location,
			'target': order.to_location,
			'route': list(order.route.edges.all()),
			'position': order.route.active_edge_index,
			'weight': order.route.get_active_edge().edge_type_id.max_weight
		}

		return order_info

	def make_order(self, data):
		print('*********************************')
		print(data)
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
