from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Delivery(models.Model):
    STATUS = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    )
    sender_first_name = models.CharField("First name", max_length=50)
    sender_last_name = models.CharField("Last name", max_length=50, blank=True)
    sender_contact = models.IntegerField("Contact")
    receiver_first_name = models.CharField("First name", max_length=50)
    receiver_last_name = models.CharField("Last name", max_length=50, blank=True)
    receiver_contact = models.IntegerField("Contact")
    items = models.TextField(max_length=255) 
    route = models.CharField(max_length=255)
    rider = models.CharField(max_length=100)
    delivery_date = models.DateField("Date", default=timezone.now, blank=True)
    departure = models.TimeField(default=timezone.now, blank=True)
    arrival = models.TimeField(default=timezone.now, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_status = models.CharField(max_length=20, choices=STATUS)
    remarks = models.TextField(max_length=255, blank=True, null=True)
    added_at = models.DateTimeField("Entry Date", default=timezone.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
    def __str__(self):
        return self.sender_first_name

    def get_absolute_url(self):
        return reverse('home')  #only use kwargs when you are redirecting to details view WHICH REQUIRES pk or id