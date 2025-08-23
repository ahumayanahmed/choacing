from django.shortcuts import render, redirect
from .models import Student

from django.shortcuts import render, redirect
from .models import Student

def admission_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        student_class = request.POST.get("student_class")
        departments = request.POST.get("departments")
        roll = request.POST.get("roll")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        # Check required fields
        if not all([name, father_name, mother_name, student_class, departments, roll, address, phone]):
            return render(request, "admissionfrom.html", {"error": "All fields are required!"})

        # Roll number validation
        try:
            roll = int(roll)
        except ValueError:
            return render(request, "admissionfrom.html", {"error": "Roll must be a number!"})

        # Save to database
        Student.objects.create(
            name=name,
            father_name=father_name,
            mother_name=mother_name,
            student_class=student_class,
            departments=departments,
            roll=roll,
            address=address,
            phone=phone
        )

        return redirect("homepage")  # homepage URL name

    return render(request, "admissionfrom.html")


#student result view

from django.shortcuts import render
from .models import Student

def infirmationchack(request):
    error = ""
    student = None
    results = []
    total = 0

    if request.method == "POST":
        # POST data get করা
        name = request.POST.get("name", "").strip()
        father_name = request.POST.get("father", "").strip()
        mother_name = request.POST.get("mother", "").strip()
        student_class = request.POST.get("class", "").strip()
        roll = request.POST.get("roll", "").strip()
        departments = request.POST.get("departments", "").strip()

        # সব field filled কি না চেক
        if all([name, father_name, mother_name, student_class, roll, departments]):
            try:
                # Database এ student খুঁজে বের করা
                student = Student.objects.get(
                    name__iexact=name,
                    father_name__iexact=father_name,
                    mother_name__iexact=mother_name,
                    student_class__iexact=student_class,
                    roll=roll,
                    departments__iexact=departments
                  )
                # Student এর সাথে তার result গুলো নিয়ে আসা
                results = student.results.all()
                total = sum(r.marks for r in results)

                return render(request, "student.html", {
                    "student": student,
                    "results": results,
                    "total": total
                })

            except Student.DoesNotExist:
                error = "No student information found!"
        else:
            error = "All fields are required!"

    # GET request বা invalid POST → form page render
    return render(request, "studentresult.html", {"error": error})
