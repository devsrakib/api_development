# from django.urls import reverse
# from myapp.models import Contact
# from myapp.serializers import ContactSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin,
# )
# from rest_framework.generics import GenericAPIView
# from rest_framework.authentication import (
#     SessionAuthentication,
#     BasicAuthentication,
#     TokenAuthentication,
# )
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import renderers


# # Create your views here.
# class contactList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class contactDetails(
#     RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
# ):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     lookup_field = "pk"
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class api_root(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(
#             {
#                 "contacts": reverse("contact-list", request=request),
#             }
#         )


from rest_framework import generics
from .models import Owner, Customer, Supplier, TodaySell
from .serializers import (
    OwnerSerializer,
    CustomerSerializer,
    SupplierSerializer,
    TodaySellSerializer,
)
from myapp.pagination import CustomerPagination, OwnerPagination
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class OwnerCreateView(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = OwnerPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OwnerList(generics.GenericAPIView, ListModelMixin):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = OwnerPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OwnerDetailView(UpdateModelMixin, generics.ListAPIView):
    serializer_class = OwnerSerializer
    lookup_field = "id"

    def get_queryset(self):
        id = self.kwargs["id"]
        return Owner.objects.filter(id=id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteOwner(DestroyModelMixin, generics.GenericAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomerListCreateView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerByOwnerView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

    def get_queryset(self):
        owner_id = self.kwargs["owner_id"]
        return Customer.objects.filter(owner=owner_id)


class SupplierListCreateView(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodaySellListCreateView(generics.ListCreateAPIView):
    queryset = TodaySell.objects.all()
    serializer_class = TodaySellSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "id"


class TodaySellDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodaySell.objects.all()
    serializer_class = TodaySellSerializer
    lookup_field = "id"
