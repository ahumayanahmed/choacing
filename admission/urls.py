from django.urls import path
from . import views

urlpatterns = [
    path('admission_form/', views.admission_form, name='admission_form'),
    path('infirmationchack', views.infirmationchack, name='infirmationchack'),
   
]
