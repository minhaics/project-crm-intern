# Create your models here.
from django.db import models
from customers.models import Customer
from products.models import Product

class Lead(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="leads")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="leads")
    status = models.CharField(max_length=50, choices=[
        ('New', 'New'),
        ('Won', 'Won'),
        ('Lost', 'Lost')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lead: {self.customer.name} -> {self.product.name} ({self.status})"
