from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cars.models import CarConfiguration
from shop.models import Order

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    # Get user's car configurations
    car_configurations = CarConfiguration.objects.filter(user=request.user).order_by('-created_at')

    # Get user's orders
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'car_configurations': car_configurations,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)