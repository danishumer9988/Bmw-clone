from django.contrib import admin
from .models import Car, CarConfiguration

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'horsepower', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']

@admin.register(CarConfiguration)
class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = ['car', 'user', 'color', 'wheels', 'interior', 'created_at']
    list_filter = ['car', 'color', 'wheels', 'interior']