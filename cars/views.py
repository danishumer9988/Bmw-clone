from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Car, CarConfiguration
from .forms import CarConfigurationForm

def car_list(request):
    cars = Car.objects.all()
    category = request.GET.get('category')

    if category:
        cars = cars.filter(category=category)

    categories = dict(Car.CATEGORY_CHOICES)

    context = {
        'cars': cars,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'cars/car_list.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    similar_cars = Car.objects.filter(category=car.category).exclude(id=car.id)[:3]

    context = {
        'car': car,
        'similar_cars': similar_cars,
    }
    return render(request, 'cars/car_detail.html', context)

@login_required
def configurator(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarConfigurationForm(request.POST)
        if form.is_valid():
            configuration = form.save(commit=False)
            configuration.car = car
            configuration.user = request.user
            configuration.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CarConfigurationForm()

    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'cars/configurator.html', context)