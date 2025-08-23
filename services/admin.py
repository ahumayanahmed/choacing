from django.contrib import admin
from django.contrib import admin
from .models import homepage_banner,services_page,homepage_box, footer,class_routine,homepage_box2

# Register your models here.
class spage(admin.ModelAdmin):
    list_display=('sevices','ervices_heder')

class ban(admin.ModelAdmin):
    list_display=('banner',)



class homebox(admin.ModelAdmin):
    list_display=('box_header','photo')


class foter(admin.ModelAdmin):
    list_display=('title','facbook','twitter','instagram','youtube','linkdin','github')


class crout(admin.ModelAdmin):
    list_display=('titel','photo')

class homebox2(admin.ModelAdmin):
    list_display=('box_header','sevices')

# Register your models here.

admin.site.register(services_page,spage)
admin.site.register(homepage_box,homebox)
admin.site.register(homepage_box2,homebox2)
admin.site.register(footer,foter)
admin.site.register(class_routine,crout)
admin.site.register(homepage_banner,ban)
