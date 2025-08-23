from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='reg'), 
    path('homepage/', views.regview, name='homepage'), 
    path('log/', views.loging, name='log'),
    path('logout/', views.logout_view, name='logout'),
    path('passwordchange/', views.password_change, name='passc'),
    path('forgot/', views.forgot_password, name='forgot_password'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('profile_update/', views.profile_settings, name='profile_settings'),
    path('profileview/', views.profileview, name='profileview'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
