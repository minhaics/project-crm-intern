from rest_framework import serializers
from .models import SupportTicket


class SupportTicketSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta:
        model = SupportTicket
        fields = ['id', 'customer', 'customer_name', 'subject',
                  'description', 'status', 'created_at', 'updated_at']
