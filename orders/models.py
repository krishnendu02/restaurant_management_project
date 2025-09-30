from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    discount = models.DecimalField(max_digits=5, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)

class OrderStatus(models.Model):
    name = models.CharField(max_length = 50, unique = True)

class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus,
        on_delete= models.SET_NULL,
        null = True,
        blank = True,
        related_name = "orders"
    )

def __str__(self):
    return self.code

def __str__(self):
    return self.name

def __str__(self):
    return f"Order #{self.id} - {self.status.name if self.status else 'No Status'}"