from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    # Determine which fields to display
    list_display = (
        'sender_first_name', 
        'sender_last_name', 
        'sender_contact', 
        'receiver_first_name', 
        'receiver_last_name',
        'receiver_contact',
        'route',
        'delivery_status',
        )

    # Display a filter by the side
    list_filter = ['delivery_status', 'delivery_date', 'rider']

admin.site.register(Delivery, DeliveryAdmin)
