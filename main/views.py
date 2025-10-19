from django.shortcuts import render
from cars.models import Car
from news.models import Post

def home(request):
    # Get featured cars (you might want to add a 'featured' field to Car model)
    featured_cars = Car.objects.all()[:3]

    # Get latest news
    latest_news = Post.objects.filter(published=True).order_by('-created_at')[:3]

    context = {
        'featured_cars': featured_cars,
        'latest_news': latest_news,
    }
    return render(request, 'home.html', context)