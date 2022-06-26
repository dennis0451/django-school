
from http.client import HTTPResponse
from django.shortcuts import render
from .models import School  # import our School class

my_school = School("Django School")  # create a school instance


def index(request):
    my_data = { "school": my_school}
    return render(request, "school_interface/index.html", my_data)

def list_staff(request):

    all_staff = { 'all_staff' : my_school.staff }
    return render(request, "school_interface/list_staff.html", all_staff)


def staff_detail(request, employee_id):
    employee = my_school.find_staff_by_id(employee_id)
    employee_data = {'employee': employee}
    
    return render(request, "school_interface/staff_detail.html", employee_data)

def list_students(request):
    all_students = {'all_students' : my_school.students}
    return render(request, "school_interface/list_students.html", all_students)

def student_detail(request, school_id):
    student = my_school.find_student_by_id(school_id)
    student_data = {'student' : student}
    return render(request, 'school_interface/student_detail.html', student_data)