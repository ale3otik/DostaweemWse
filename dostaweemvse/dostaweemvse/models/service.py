from .delivery_base import DeliveryBase
from .graph import Graph
from .order import Order
from .location import Location

class Service(object):
	delivery_base = DeliveryBase()

	@staticmethod
	def get_order_info(order_id):
		try:
			order = delivery_base.get_order(order_id)
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
	@staticmethod
	def make_order(data):
		_from = Location.objects.filter(location_name=data['source'])
		_to = Location.objects.filter(location_name=data['target'])
		_route = None
		_max_cost = int(data['weight'])

		if 'meta' in data.keys():
			_metadata = data['meta']
		else:
			_metadata = ""

		_order = Order(
			route=_route,
			metadata=_metadata,
			from_location=_from,
			to_location=_to,
			max_cost=_max_cost
			)

		_route = Graph.build_route(_order)

		if _route:
			_route.save()
			_order.route = _route
			_order.save()

			delivery_base.save_order(_order)
			delivery_base.save()

		else:
			raise RuntimeError()
