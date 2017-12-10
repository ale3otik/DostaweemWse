from django.db import models

class DeliveryBase(models.model):
	orders = models.ManyToManyField(Order)

	def save_order(order):
		self.orders.add(order)


	def get_order(order_id):
		return self.orders.all().get(pk=order_id)