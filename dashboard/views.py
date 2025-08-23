from django.shortcuts import render
from django.db.models import Avg
from admission.models import Teacher, Student, Result
from django.shortcuts import render
from django.db.models import Count
from services.models import class_routine
# Create your views here.

from django.db.models import Count

def dashboard(request):
    # Dynamic Teacher counts by department
    teacher_departments = Teacher.objects.values_list('department', flat=True).distinct()
    teacher_counts = {}
    total_teacher = Teacher.objects.count()
    for dept in teacher_departments:
        teacher_counts[dept] = Teacher.objects.filter(department=dept).count()

    # Dynamic Student counts by class and department
    student_classes = Student.objects.values_list('student_class', flat=True).distinct()
    student_counts = {}
    for cls in student_classes:
        student_counts[cls] = {}
        student_counts[cls]['total'] = Student.objects.filter(student_class=cls).count()
        student_departments = Student.objects.filter(student_class=cls).values_list('departments', flat=True).distinct()
        for dept in student_departments:
            student_counts[cls][dept] = Student.objects.filter(student_class=cls, departments=dept).count()

    # Routine
    routine = class_routine.objects.all()

    # Results
    students = Student.objects.all()
    perfect_gpa_count = 0
    students_pass_count = 0
    students_fail_count = 0
    for student in students:
        results = student.results.all()
        if not results.exists():
            continue

        if all(r.marks >= 33 for r in results):
            students_pass_count += 1
        else:
            students_fail_count += 1

        if all(r.marks >= 80 for r in results):
            perfect_gpa_count += 1

    context = {
        "total_teacher": total_teacher,
        "teacher_counts": teacher_counts,
        "student_counts": student_counts,
        "students_pass_count": students_pass_count,
        "students_fail_count": students_fail_count,
        "perfect_gpa_count": perfect_gpa_count,
        "routine": routine,
    }
    return render(request, "dashboard.html", context)
