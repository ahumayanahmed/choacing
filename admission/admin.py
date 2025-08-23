from django.contrib import admin
from .models import Teacher,Student,Result

# Register your models here.
class te(admin.ModelAdmin):
    list_display=('name','qualifications','address','phone','department','photo')
    

class st(admin.ModelAdmin):
    list_display=('name','father_name','mother_name','student_class','roll','address','phone','departments','photo')

class Re(admin.ModelAdmin):
    list_display=('student','subject','marks','grade') 
    list_display_links = ('student', 'subject')
  


admin.site.register(Teacher,te)
admin.site.register(Student,st)
admin.site.register(Result,Re)

