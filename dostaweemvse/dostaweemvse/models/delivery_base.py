from django.db import models
from .order import Order

class DeliveryBase(models.model):
	orders = models.ManyToManyField(Order)

	def save_order(order):
		orders.add(order)

	def get_order(order_id):
		return orders.all().get(pk=order_id)