from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('main/', include('main.urls')),
                  path('cars/', include('cars.urls')),
                  path('shop/', include('shop.urls')),
                  path('news/', include('news.urls')),
                  path('users/', include('users.urls')),
                  path('contact/', include('contact.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)