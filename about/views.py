from django.shortcuts import render, get_object_or_404
from admission.models import Teacher

# Create your views here.
def student_info(request):
    return render(request, 'student.html')




def teacher_info(request):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers}  # plural
    return render(request, 'teacher.html', context)



def teacher_by_department(request, department):
    # database থেকে department অনুযায়ী filter
    teachers = Teacher.objects.filter(department__iexact=department)
    
    context = {
        "department": department,
        "teachers": teachers
    }
    return render(request, "teacher_department.html", context)

def department_list(request):
    departments = Teacher.objects.values_list("department", flat=True).distinct()
    print("Departments in DB:", list(departments))   # Debugging
    return render(request, "departments.html", {"departments": departments})



    