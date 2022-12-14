from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,"Bronze"),
        (MEMBERSHIP_SILVER,"Silver"),
        (MEMBERSHIP_GOLD,"Gold"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PAYMENTSTATUS_PENDING = 'P'
    PAYMENTSTATUS_COMPLETE = 'C'
    PAYMENTSTATUS_FAILED = 'F'

    PAYMENTSTATUS_CHOICES = [
        (PAYMENTSTATUS_PENDING, 'Pending'),
        (PAYMENTSTATUS_COMPLETE, 'Complete'),
        (PAYMENTSTATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateField(auto_now_add=True, null=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENTSTATUS_CHOICES, default=PAYMENTSTATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.models.CharField(max_length=255)
    city = models.models.CharField(max_length=255)
    customer = models.Foreign_key(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForignKey(Cart, on_delete=models.CASCADE)
    product = models.ForignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


