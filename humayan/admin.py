from django.contrib import admin
from .models import registrations

# Register your models here.
class paymn(admin.ModelAdmin):
    list_display=('Name','Email','Pass')
    
admin.site.register(registrations,paymn)
