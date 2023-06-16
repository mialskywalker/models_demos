from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department_id=1).filter(age__gt=30).order_by('age')
    # departments = Department.objects.all()

    context = {
        "employees": employees,
        "employees2": employees2,
    }

    return render(request, "web/index.html", context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    # return render(request, "web/delete_employee.html")
    return redirect("index")
