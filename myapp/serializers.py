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
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "profile_photo",
            "createAt",
            "owner",
        ]


# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "phone", "profile_photo", "createAt", "owner"]


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
            "createdAt",
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
    cash_sell = CashSellSerializer(read_only=True)
    cash_buy = CashBuySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "due",
            "extra_amount",
            "description",
            "date",
            "cash_sell",
            "cash_buy",
        ]


# Lend Given Serializer
class LendGivenSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = LendGiven
        fields = ["id", "amount", "date", "description", "customer"]


# Borrow Taken Serializer
class BorrowTakenSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = BorrowTaken
        fields = ["id", "amount", "date", "description", "customer"]


# Deposit Serializer
class DepositSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Deposit
        fields = ["id", "amount", "date", "description", "owner"]


# Expense Serializer
class ExpenseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ["id", "amount", "date", "owner"]


# Match Cash Box Serializer
class MatchCashBoxSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = MatchCashBox
        fields = ["id", "total_amount", "date", "owner"]


# Withdraw Serializer
class WithdrawSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Withdraw
        fields = ["id", "amount", "date", "description", "owner"]


# Collection Reminder Serializer
class CollectionReminderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = CollectionReminder
        fields = ["id", "collection_date", "date", "amount", "customer", "supplier"]
