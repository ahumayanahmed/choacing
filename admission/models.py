from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)  # Science / Arts / Commerce
    photo = models.ImageField(upload_to="teachers/",blank=True, default="")

# Student Table
class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)   # যেমন: Class 8
    departments = models.CharField(max_length=50,blank=True, null=True)  # Science / Arts / Commerce
    roll = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="students/",blank=True, default="")  # Student Image

  

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)




       # grade ও GPA auto হিসাব হবে
    def calculate_grade_gpa(self):
        if self.marks >= 80:
            return "A+", 5.00
        elif self.marks >= 70:
            return "A", 4.00
        elif self.marks >= 60:
            return "A-", 3.50
        elif self.marks >= 50:
            return "B", 3.00
        elif self.marks >= 40:
            return "C", 2.00
        elif self.marks >= 33:
            return "D", 1.00
        else:
            return "F", 0.00

    @property
    def grade(self):
        return self.calculate_grade_gpa()[0]

    @property
    def gpa(self):
        return self.calculate_grade_gpa()[1]

    def __str__(self):
        return f"{self.student.name} - {self.subject} ({self.grade})"