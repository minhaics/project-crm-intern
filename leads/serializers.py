from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'customer', 'customer_name', 'product',
                  'product_name', 'status', 'created_at', 'updated_at']
