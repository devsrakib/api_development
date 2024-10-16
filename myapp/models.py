from django.db import models
import uuid


class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customerName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    owner = models.ForeignKey(Owner, related_name="customers", on_delete=models.CASCADE)

    def __str__(self):
        return self.customerName


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    owner = models.ForeignKey(Owner, related_name="suppliers", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TodaySell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sell_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2)
    extra_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    due = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(
        Customer, related_name="today_sells", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Sale by {self.customer.customerName} - Amount: {self.sell_amount}"
