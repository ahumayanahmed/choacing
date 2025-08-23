from django.shortcuts import render
from .models import services_page

# Create your views here.
def services(request):
    serv= services_page.objects.all()
    context={
        'serv':serv,
    }
    return render(request, 'service.html',context)




#search er jonno

from django.shortcuts import render
from django.http import JsonResponse
from admission.models import Teacher, Student
from django.db.models import Q


def search(request):
    query = request.GET.get('q', '')

    teachers = Teacher.objects.filter(
        Q(name__icontains=query) | Q(department__icontains=query)
    ) if query else Teacher.objects.none()

    students = Student.objects.filter(
        Q(name__icontains=query) | Q(student_class__icontains=query)
    ) if query else Student.objects.none()

    context = {
        'query': query,
        'teachers': teachers,
        'students': students,
    }

    return render(request, 'search.html', context)
