from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('dealers/', views.dealer_locator, name='dealer_locator'),
]