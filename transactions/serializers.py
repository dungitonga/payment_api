from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'customer_email', 'payment_amount']
        read_only_fields = ['id']

