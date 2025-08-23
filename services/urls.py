from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('services/', views.services, name='services'),
    path('search/', views.search, name='search'),
]

