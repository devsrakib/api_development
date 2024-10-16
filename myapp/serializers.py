from rest_framework import serializers
from .models import Owner, Customer, Supplier, TodaySell


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "name", "email", "phone", "photo"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "customerName", "email", "owner"]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "owner"]


class TodaySellSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodaySell
        fields = [
            "id",
            "sell_amount",
            "collected_amount",
            "extra_amount",
            "due",
            "customer",
        ]
