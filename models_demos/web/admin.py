from django.contrib import admin
from .models import Employee, Department, Salary


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    pass
