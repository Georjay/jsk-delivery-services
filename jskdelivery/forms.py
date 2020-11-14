from django.forms import ModelForm
from .models import Delivery
from django import forms

class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'

class new_entryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'sender_first_name', 
            'sender_last_name', 
            'sender_contact', 
            'receiver_first_name', 
            'receiver_last_name', 
            'receiver_contact', 
            'items', 
            'amount', 
            'route', 
            'rider',
            'delivery_date',
            'departure', 
            'arrival',
            'delivery_status', 
            'remarks'
            ]
        widgets = {
            'delivery_date': DateInput,
            'departure': TimeInput,
            'arrival' : TimeInput,
        }
