from .models.delivery_base import DeliveryBase
from .graph import Graph
from .models.order import Order

class Service(object):
	def get_order_info(self, order_id):
		self.delivery_base = DeliveryBase()

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
		_from = data['source']
		_to = data['target']
		_route = None
		_max_cost = data['weight']

		if 'meta' in data.keys():
			_metadata = data['meta']
		else:
			_metadata = ""
	
		_order = Order(_route, _metadata, _from, _to, _max_cost)
		_route = Graph.build_route(_order)
		
		if _route:
			_route.save()
			_order.route = _route
			_order.save()

			self.delivery_base.save_order(_order)
			self.delivery_base.save()

		else:
			raise RuntimeError()