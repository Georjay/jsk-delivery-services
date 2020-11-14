from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( 
    ListView, 
    CreateView,
    UpdateView,
)
from .models import Delivery
from .forms import new_entryForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Sum, Value as V #To sum the amount of money
from chartit import DataPool, Chart
from django.db.models.functions import Coalesce


# Create your views here.
class DeliveryListView(LoginRequiredMixin, ListView):
    model = Delivery
    template_name = 'jskdelivery/home.html'
    context_object_name = 'deliveries'
    ordering = ['-id']


class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    form_class = new_entryForm #This allowed me specify the fields in forms.py

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Delivery
    form_class = new_entryForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def dashboard(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    deliveries = \
        DataPool(
           series=
            [{'options': {
               'source': Delivery.objects.filter(added_at__gte=timezone.now()-timedelta(days=30))},
              'terms': [
                'amount' ]}
             ])
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = deliveries,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms': { 
                    'amount': [
                        'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Amount (Last 30 Days)'},
               'xAxis': {
                    'title': {
                       'text': 'Amount'}}})

    all_deliveries = Delivery.objects.all().count()
    todays_deliveries = Delivery.objects.filter(added_at__date=date.today()).count()
    last_seven_days = Delivery.objects.filter(added_at__gte=timezone.now()-timedelta(days=7)).count() #I replaced 'datetime' with 'timezone' to avoid a runtime error
    last_30_days = Delivery.objects.filter(added_at__gte=timezone.now()-timedelta(days=30)).count()
    total_amount = Delivery.objects.aggregate(sum=Coalesce(Sum('amount'), V(0))).get('sum')
    total_amount_last_7_days = Delivery.objects.filter(added_at__gte=timezone.now()-timedelta(days=7)).aggregate(sum=Coalesce(Sum('amount'), V(0))).get('sum')
    
    template = 'jskdelivery/dashboard.html'
    context = {
        'cht_list': cht,
        'all_deliveries': all_deliveries,
        'todays_deliveries': todays_deliveries,
        'last_seven_days': last_seven_days,
        'last_30_days': last_30_days,
        'total_amount': total_amount,
        'total_amount_last_7_days': total_amount_last_7_days,
    }
    
    return render(request, template, context)
