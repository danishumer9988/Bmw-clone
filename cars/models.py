from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('M', 'M Series'),
        ('X', 'X Series'),
        ('I', 'i Series'),
        ('Z', 'Z Series'),
        ('OTHER', 'Other Series'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    horsepower = models.IntegerField()
    acceleration = models.DecimalField(max_digits=4, decimal_places=1)
    top_speed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CarConfiguration(models.Model):
    COLOR_CHOICES = [
        ('alpine_white', 'Alpine White'),
        ('black_sapphire', 'Black Sapphire'),
        ('mineral_grey', 'Mineral Grey'),
        ('tanzanite_blue', 'Tanzanite Blue'),
        ('sao_paulo_yellow', 'São Paulo Yellow'),
    ]

    WHEEL_CHOICES = [
        ('standard', 'Standard 18"'),
        ('sport', 'Sport 19"'),
        ('premium', 'Premium 20"'),
        ('performance', 'Performance 21"'),
    ]

    INTERIOR_CHOICES = [
        ('sensatec_black', 'Sensatec Black'),
        ('vernasca_cognac', 'Vernasca Cognac'),
        ('merino_black', 'Merino Black'),
        ('individual_white', 'Individual White'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    wheels = models.CharField(max_length=20, choices=WHEEL_CHOICES)
    interior = models.CharField(max_length=20, choices=INTERIOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.name} - {self.user.username}"