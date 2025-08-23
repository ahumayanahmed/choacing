from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student/', views.student_info, name='student'),
    path('teacher/', views.teacher_info, name='teacher'),
    path("departments/", views.department_list, name="department_list"),
    path("teachers/<str:department>/", views.teacher_by_department, name="teacher_by_department"),
]


