from django.urls import path
from .views import (
    create_retrieve_owner,
    CustomerListCreateView,
    CustomerDetailView,
    SupplierListCreateView,
    SupplierDetailView,
    CashSellListCreateView,
    CashSellDetailView,
    CashBuyListCreateView,
    CashBuyDetailView,
    TransactionListCreateView,
    TransactionDetailView,
    LendGivenListCreateView,
    LendGivenDetailView,
    BorrowTakenListCreateView,
    BorrowTakenDetailView,
    DepositListCreateView,
    DepositDetailView,
    ExpenseListCreateView,
    ExpenseDetailView,
    MatchCashBoxListCreateView,
    MatchCashBoxDetailView,
    WithdrawListCreateView,
    WithdrawDetailView,
    CollectionReminderListCreateView,
    CollectionReminderDetailView,
)

urlpatterns = [
    # Owner URLs
    path("owners/", create_retrieve_owner, name="owner-list-create"),
    path("owners/<uuid:id>/", create_retrieve_owner, name="owner-detail"),
    # Customer URLs
    path("customers/", CustomerListCreateView.as_view(), name="customer-list-create"),
    path("customers/<uuid:id>/", CustomerDetailView.as_view(), name="customer-detail"),
    # Supplier URLs
    path("suppliers/", SupplierListCreateView.as_view(), name="supplier-list-create"),
    path("suppliers/<uuid:id>/", SupplierDetailView.as_view(), name="supplier-detail"),
    # Cash Sell URLs
    path("cash-sells/", CashSellListCreateView.as_view(), name="cash-sell-list-create"),
    path(
        "cash-sells/<uuid:id>/", CashSellDetailView.as_view(), name="cash-sell-detail"
    ),
    # Cash Buy URLs
    path("cash-buys/", CashBuyListCreateView.as_view(), name="cash-buy-list-create"),
    path("cash-buys/<uuid:id>/", CashBuyDetailView.as_view(), name="cash-buy-detail"),
    # Transaction URLs
    path(
        "transactions/",
        TransactionListCreateView.as_view(),
        name="transaction-list-create",
    ),
    path(
        "transactions/<uuid:id>/",
        TransactionDetailView.as_view(),
        name="transaction-detail",
    ),
    # Lend Given URLs
    path(
        "lend-given/", LendGivenListCreateView.as_view(), name="lend-given-list-create"
    ),
    path(
        "lend-given/<uuid:id>/", LendGivenDetailView.as_view(), name="lend-given-detail"
    ),
    # Borrow Taken URLs
    path(
        "borrow-taken/",
        BorrowTakenListCreateView.as_view(),
        name="borrow-taken-list-create",
    ),
    path(
        "borrow-taken/<uuid:id>/",
        BorrowTakenDetailView.as_view(),
        name="borrow-taken-detail",
    ),
    # Deposit URLs
    path("deposits/", DepositListCreateView.as_view(), name="deposit-list-create"),
    path("deposits/<uuid:id>/", DepositDetailView.as_view(), name="deposit-detail"),
    # Expense URLs
    path("expenses/", ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("expenses/<uuid:id>/", ExpenseDetailView.as_view(), name="expense-detail"),
    # Match Cash Box URLs
    path(
        "match-cash-boxes/",
        MatchCashBoxListCreateView.as_view(),
        name="match-cash-box-list-create",
    ),
    path(
        "match-cash-boxes/<uuid:id>/",
        MatchCashBoxDetailView.as_view(),
        name="match-cash-box-detail",
    ),
    # Withdraw URLs
    path("withdraws/", WithdrawListCreateView.as_view(), name="withdraw-list-create"),
    path("withdraws/<uuid:id>/", WithdrawDetailView.as_view(), name="withdraw-detail"),
    # Collection Reminder URLs
    path(
        "collection-reminders/",
        CollectionReminderListCreateView.as_view(),
        name="collection-reminder-list-create",
    ),
    path(
        "collection-reminders/<uuid:id>/",
        CollectionReminderDetailView.as_view(),
        name="collection-reminder-detail",
    ),
]
