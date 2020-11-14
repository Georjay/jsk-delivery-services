from django.urls import path
from .views import DeliveryListView, DeliveryCreateView, DeliveryUpdateView
from . import views

urlpatterns = [
    path('', DeliveryListView.as_view(), name='home'),
    path('delivery/new/', DeliveryCreateView.as_view(), name='delivery-create'), #this url will share a view with the update form
    path('delivery/<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery-update'),
    path('dashboard/', views.dashboard, name='dashboard'),
]