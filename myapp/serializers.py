from rest_framework import serializers
from .models import (
    Owner,
    Customer,
    Supplier,
    CashSell,
    CashBuy,
    Transaction,
    LendGiven,
    BorrowTaken,
    Deposit,
    Expense,
    MatchCashBox,
    Withdraw,
    CollectionReminder,
)


# Owner Serializer
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "name", "email", "phone", "profile_photo"]


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    # owner = OwnerSerializer(read_only=True)
    # c_owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "profile_photo",
            "createdAt",
            "owner",
        ]


# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "phone", "profile_photo", "createdAt", "owner"]


# Cash Sell Serializer
class CashSellSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = CashSell
        fields = [
            "id",
            "sell_amount",
            "collected_amount",
            "description",
            "customer",
        ]


# Cash Buy Serializer
class CashBuySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = CashBuy
        fields = [
            "id",
            "sell_amount",
            "collected_amount",
            "description",
            "createdAt",
            "supplier",
        ]


# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    # cash_sell = CashSellSerializer(read_only=True)
    # cash_buy = CashBuySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "due",
            "extra_amount",
            "description",
            "cashsell",
        ]

    def to_representation(self, instance):
        cashsell = instance.cashsell  #
        if cashsell:
            due = cashsell.sell_amount - cashsell.collected_amount
            extra_amount = 0 if due > 0 else -due
            instance.due = due
            instance.extra_amount = extra_amount
        return super().to_representation(instance)


# Lend Given Serializer
class LendGivenSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = LendGiven
        fields = ["id", "amount", "createdAt", "description", "customer"]


# Borrow Taken Serializer
class BorrowTakenSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = BorrowTaken
        fields = ["id", "amount", "createdAt", "description", "customer"]


# Deposit Serializer
class DepositSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Deposit
        fields = ["id", "amount", "createdAt", "description", "owner"]


# Expense Serializer
class ExpenseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ["id", "amount", "createdAt", "owner"]


# Match Cash Box Serializer
class MatchCashBoxSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = MatchCashBox
        fields = ["id", "total_amount", "createdAt", "owner"]


# Withdraw Serializer
class WithdrawSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Withdraw
        fields = ["id", "amount", "createdAt", "description", "owner"]


# Collection Reminder Serializer
class CollectionReminderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = CollectionReminder
        fields = [
            "id",
            "collection_date",
            "amount",
            "customer",
        ]
