from django.db import models
from .order import Order

class DeliveryBase(models.Model):
	orders = models.ManyToManyField(Order)

	def save_order(self, order):
		self.orders.add(order)

	def get_order(self, order_id):
		return self.orders.all().get(pk=order_id)
