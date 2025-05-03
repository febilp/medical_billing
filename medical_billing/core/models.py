# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('inventory', 'inventory Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Medicine(models.Model):
    PACKAGING_CHOICES = [
        ('piece', 'Piece'),
        ('strip', 'Strip'),
        ('pack', 'Pack'),
        ('box', 'Box'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    expiry_date = models.DateField()
    packaging_types = models.CharField(max_length=10, choices=PACKAGING_CHOICES, default='strip')
    price_piece = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_strip = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_pack = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_box = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Bill(models.Model):
    staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    packaging_type = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
