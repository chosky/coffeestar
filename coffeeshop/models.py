from django.db import models
from django.utils import timezone

class departament(models.Model):
	id_dpto = models.IntegerField(primary_key = True)
	dpto_name = models.CharField(max_length=30, unique = True)

	
	def __str__(self):
		return self.dpto_name


class city(models.Model):
	id_city = models.IntegerField(primary_key = True)
	city_name = models.CharField(max_length=30, unique = True)
	id_dpto = models.ForeignKey(departament, on_delete = models.CASCADE)


	def __str__(self):
		return self.city_name


class provider(models.Model):
	id_provider = models.IntegerField(primary_key = True)
	provider_name = models.CharField(max_length = 30)
	tel_provider = models.IntegerField(unique = True)
	id_city = models.ForeignKey(city, on_delete = models.CASCADE)


	def __str__(self):
		return self.provider_name


class client(models.Model):
	name_client = models.CharField(max_length=20)
	id_client = models.IntegerField(primary_key = True)
	id_city = models.ForeignKey(city, on_delete = models.CASCADE)


	def __str__(self):
		return self.name_client


class description_bill_payment(models.Model):
	payment_modes = {
			('CC', 'Credit Card'),
			('CM', 'Cash Money'),
			}

	id_payment = models.IntegerField(primary_key = True)
	pay_mode = models.CharField(max_length = 2, choices = payment_modes, default = 'CM')
	employee_name = models.CharField(max_length=20)


	def __str__(self):
		return str(self.id_payment)


class bill_payment(models.Model):
	id_bill_payment = models.IntegerField(primary_key = True)
	id_client = models.ForeignKey(client, on_delete = models.CASCADE)
	id_payment = models.ForeignKey(description_bill_payment, on_delete = models.CASCADE)
	payment_date = models.DateTimeField()
	

	def __str__(self):
		return self.id_bill_payment



class product_type(models.Model):
	id_product_type = models.IntegerField(primary_key = True)
	product_type = models.CharField(max_length = 30, unique = True)
	product_description = models.TextField(max_length = 50)
	
	
	def __str__(self):
		return self.id_product_type



class product(models.Model):
	id_product = models.IntegerField(primary_key = True)
	name_product = models.CharField(max_length = 20, unique = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 7)
	stock = models.IntegerField()
	id_provider = models.ForeignKey(provider, on_delete = models.CASCADE)
	id_product_type = models.ForeignKey(product_type, on_delete = models.CASCADE)

	def __str__(self):
		return self.name_product



class sale(models.Model):
	id_sale = models.IntegerField(primary_key = True)
	id_bill_payment = models.ForeignKey(bill_payment, on_delete = models.CASCADE)
	quantity_sold = models.IntegerField()
	id_product = models.ForeignKey(product, on_delete = models.CASCADE)
	sale_value = models.DecimalField(max_digits = 10, decimal_places = 5)


	def __str__(self):
		return self.id_sale
