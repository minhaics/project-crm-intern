# Create your models here.
from django.db import models
from customers.models import Customer
from products.models import Product


class Transaction(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="transactions")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="transactions")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled')
    ])

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"
