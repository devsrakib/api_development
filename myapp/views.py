from rest_framework import generics
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
from .serializers import (
    OwnerSerializer,
    CustomerSerializer,
    SupplierSerializer,
    CashSellSerializer,
    CashBuySerializer,
    TransactionSerializer,
    LendGivenSerializer,
    BorrowTakenSerializer,
    DepositSerializer,
    ExpenseSerializer,
    MatchCashBoxSerializer,
    WithdrawSerializer,
    CollectionReminderSerializer,
)


# Owner Views


class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = "id"


# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"


# Supplier Views
class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "id"


# Cash Sell Views
class CashSellListCreateView(generics.ListCreateAPIView):
    queryset = CashSell.objects.all()
    serializer_class = CashSellSerializer


class CashSellDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CashSell.objects.all()
    serializer_class = CashSellSerializer
    lookup_field = "id"


# Cash Buy Views
class CashBuyListCreateView(generics.ListCreateAPIView):
    queryset = CashBuy.objects.all()
    serializer_class = CashBuySerializer


class CashBuyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CashBuy.objects.all()
    serializer_class = CashBuySerializer
    lookup_field = "id"


# Transaction Views
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"


# Lend Given Views
class LendGivenListCreateView(generics.ListCreateAPIView):
    queryset = LendGiven.objects.all()
    serializer_class = LendGivenSerializer


class LendGivenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LendGiven.objects.all()
    serializer_class = LendGivenSerializer
    lookup_field = "id"


# Borrow Taken Views
class BorrowTakenListCreateView(generics.ListCreateAPIView):
    queryset = BorrowTaken.objects.all()
    serializer_class = BorrowTakenSerializer


class BorrowTakenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowTaken.objects.all()
    serializer_class = BorrowTakenSerializer
    lookup_field = "id"


# Deposit Views
class DepositListCreateView(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class DepositDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    lookup_field = "id"


# Expense Views
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = "id"


# Match Cash Box Views
class MatchCashBoxListCreateView(generics.ListCreateAPIView):
    queryset = MatchCashBox.objects.all()
    serializer_class = MatchCashBoxSerializer


class MatchCashBoxDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchCashBox.objects.all()
    serializer_class = MatchCashBoxSerializer
    lookup_field = "id"


# Withdraw Views
class WithdrawListCreateView(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class WithdrawDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    lookup_field = "id"


# Collection Reminder Views
class CollectionReminderListCreateView(generics.ListCreateAPIView):
    queryset = CollectionReminder.objects.all()
    serializer_class = CollectionReminderSerializer


class CollectionReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectionReminder.objects.all()
    serializer_class = CollectionReminderSerializer
    lookup_field = "id"
