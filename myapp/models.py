from django.db import models
import uuid
from django.utils import timezone  # Import timezone


# Owner Model
class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=11, blank=False, null=False
    )  # Make nullable or provide a default
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    owner = models.ForeignKey(Owner, related_name="customers", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Supplier Model
class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=50)
    phone = models.CharField(
        max_length=11, blank=False, null=False
    )  # Make nullable or provide a default
    profile_photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    owner = models.ForeignKey(Owner, related_name="suppliers", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Cash Sell Model
class CashSell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sell_amount = models.BigIntegerField(null=False, blank=False)
    collected_amount = models.BigIntegerField(blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    customer = models.ForeignKey(
        Customer, related_name="cash_sells", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.sell_amount)


# Cash Buy Model
class CashBuy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sell_amount = models.BigIntegerField(null=False, blank=False)
    collected_amount = models.BigIntegerField(blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    supplier = models.ForeignKey(
        Supplier, related_name="cash_buys", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.sell_amount)


# Transaction Model
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    due = models.BigIntegerField(null=False, blank=False)
    extra_amount = models.BigIntegerField(null=False, blank=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    cash_sell = models.ForeignKey(
        CashSell,
        related_name="transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    cash_buy = models.ForeignKey(
        CashBuy,
        related_name="transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.due)


# Lend Model (Given)
class LendGiven(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    description = models.CharField(max_length=500, blank=True)
    customer = models.ForeignKey(
        Customer, related_name="lends_given", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.amount)


# Borrow Model (Taken)
class BorrowTaken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    description = models.CharField(max_length=500, blank=True)
    customer = models.ForeignKey(
        Customer, related_name="borrows_taken", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.amount)


# Deposit Model
class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    description = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(Owner, related_name="deposits", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)


# Expense Model
class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    owner = models.ForeignKey(Owner, related_name="expenses", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)


# Match Cash Box Model
class MatchCashBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    owner = models.ForeignKey(
        Owner, related_name="match_cash_boxes", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.total_amount)


# Withdraw Model
class Withdraw(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.BigIntegerField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    description = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(Owner, related_name="withdraws", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)


# Collection Reminder Model
class CollectionReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    collection_date = models.DateField(blank=False)
    createAt = models.DateTimeField(default=timezone.now)  # Fix here
    amount = models.BigIntegerField(blank=False)
    customer = models.ForeignKey(
        Customer,
        related_name="collection_reminders",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    supplier = models.ForeignKey(
        Supplier,
        related_name="collection_reminders",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.amount)
