from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)


class Employee(models.Model):
    class Meta:
        # normal ordering
        # reverse ordering (descending) - use - in front of field name
        ordering = ['-first_name']

    LEVEL_JUNIOR = 'jun'
    LEVEL_MIDDLE = 'mid'
    LEVEL_SENIOR = 'sen'
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
    )

    # CASCADE (department + all connected employees)
    # RESTRICT/PROTECT (if department has employees prevent employees deletion)
    # SET_NULL (set to null if it is optional)

    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT, null=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    description = models.TextField()

    age = models.IntegerField()
    experience = models.PositiveIntegerField()
    birth_date = models.DateField()

    created_on = models.DateTimeField(auto_now_add=True)  # only first time
    updated_on = models.DateTimeField(auto_now=True)  # each time update

    is_manager = models.BooleanField(null=True)

    email = models.EmailField()

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default=LEVEL_JUNIOR)

    # define structure into DB
    # gets data from DB via models (instances)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"ID: {self.pk}; Names: {self.full_name}"


# one model == one table in db
# defines structure
# stores data (db to python and python to db)
# do operations on db via python code

# Employee.objects.all() # SELECT (get)
# Employee.objects.filter(....) # SELECT + WHERE
# Employee.objects.create(...) # INSERT (create)
# Employee.objects.delete() # DELETE

# DJANGO ORM - object relation mapper

class Salary(models.Model):
    class Meta:
        verbose_name_plural = "Salaries"

    amount = models.PositiveIntegerField()
