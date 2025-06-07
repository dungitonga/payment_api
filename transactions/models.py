from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(unique=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # status = models.CharField(max_length=20,  default='pending')

    def __str__(self):
        return f"{self.name} - {self.email} - ${self.payment_amount:.2f}"
