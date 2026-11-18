from django.shortcuts import render, HttpResponse
from .models import Student, Department, Role, Grade, Roll_Number
from django.shortcuts import render, redirect, get_object_or_404

# ------------------------
# Home Page
# ------------------------
def index(request):
    return render(request, 'index.html')


# ------------------------
# Add Student
# ------------------------
def add(request):

    departments = Department.objects.all()
    roles = Role.objects.all()
    grades = Grade.objects.all()
    roll_numbers = Roll_Number.objects.all()

    if request.method == "POST":
        Student.objects.create(
            roll_number=Roll_Number.objects.get(id=request.POST.get('roll_number')),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            marks=request.POST.get('marks'),
            phone=request.POST.get('phone'),
            percentage=request.POST.get('percentage'),
            dept=Department.objects.get(id=request.POST.get('dept')),
            role=Role.objects.get(id=request.POST.get('role')),
            grade=Grade.objects.get(id=request.POST.get('grade'))
        )

        return HttpResponse("Student Added Successfully")

    return render(request, "add.html", {
        "departments": departments,
        "roles": roles,
        "grades": grades,
        "roll_numbers": roll_numbers
    })


# ------------------------
# Remove Student Page
# ------------------------
def Remove(request):
    students = Student.objects.all()
    return render(request, "Remove.html", {"students": students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('Remove')


# ------------------------
# Show All Students
# ------------------------
def All_stu(request):
    students = Student.objects.all()
    return render(request, "All_stu.html", {"students": students})

def update_student(request):
    students = Student.objects.all()
    departments = Department.objects.all()
    roles = Role.objects.all()
    grades = Grade.objects.all()
    roll_numbers = Roll_Number.objects.all()

    selected_student = None

    # STEP 1: When user selects a student
    if request.method == "GET" and request.GET.get("student_id"):
        selected_student = get_object_or_404(
            Student, id=request.GET.get("student_id")
        )

    # STEP 2: When user submits update form
    if request.method == "POST":
        student = get_object_or_404(Student, id=request.POST.get("student_id"))

        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.phone = request.POST.get("phone")
        student.marks = request.POST.get("marks")
        student.percentage = request.POST.get("percentage")

        student.dept = Department.objects.get(id=request.POST.get("dept"))
        student.role = Role.objects.get(id=request.POST.get("role"))
        student.grade = Grade.objects.get(id=request.POST.get("grade"))
        student.roll_number = Roll_Number.objects.get(id=request.POST.get("roll_number"))

        student.save()
        return redirect("update_student")

    return render(request, "update_student.html", {
        "students": students,
        "student": selected_student,
        "departments": departments,
        "roles": roles,
        "grades": grades,
        "roll_numbers": roll_numbers
    })