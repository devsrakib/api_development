from rest_framework import generics, mixins
from rest_framework import permissions, authentication
from .permissions import IsStaffEditorPermission
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


class OwnerListCreateView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = "id"
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        # if id is not None:
        #     return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get("name")
    #     email = serializer.validated_data.get("email")
    #     if email is None:
    #         email = name
    #     serializer.save(email=email)


create_retrieve_owner = OwnerListCreateView.as_view()


# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get("name")
    #     phone = serializer.validated_data.get("phone") or None
    #     if phone is None:
    #         phone = name
    #     serializer.save(phone=phone)


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

    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)


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
