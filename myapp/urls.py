from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path("owners/", views.OwnerListCreateView.as_view(), name="owner-list-create"),
        path(
            "customers/",
            views.CustomerListCreateView.as_view(),
            name="customer-list-create",
        ),
        path(
            "customers/<uuid:id>/",
            views.CustomerDetailView.as_view(),
            name="customer-detail",
        ),
        path(
            "suppliers/",
            views.SupplierListCreateView.as_view(),
            name="supplier-list-create",
        ),
        path(
            "suppliers/<uuid:id>/",
            views.SupplierDetailView.as_view(),
            name="supplier-detail",
        ),
        path(
            "today_sells/",
            views.TodaySellListCreateView.as_view(),
            name="today_sell-list-create",
        ),
        path(
            "today_sells/<uuid:id>/",
            views.TodaySellDetailView.as_view(),
            name="today_sell-detail",
        ),
    ]
)
