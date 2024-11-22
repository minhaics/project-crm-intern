from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'customer_name', 'product', 'product_name',
                  'quantity', 'total_price', 'transaction_date', 'status']
