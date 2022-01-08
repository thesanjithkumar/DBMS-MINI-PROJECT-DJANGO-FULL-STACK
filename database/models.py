from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse

# Create your models here.
# from django.contrib.auth import get_user_model
# User = get_user_model()

sems = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),

)

sections = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
]


class Department(models.Model):
    dept_id = models.CharField(
        max_length=10, blank=False, null=False, primary_key=True, unique=True)
    dept_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.dept_name

    def get_absolute_url(self):
        return reverse("dept_single", kwargs={"pk": self.pk})


class Student(models.Model):
    usn = models.CharField(max_length=10, blank=False,
                           null=False, primary_key=True, unique=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(
        max_length=10, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    address = models.TextField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    sem = models.CharField(choices=sems, max_length=1)
    section = models.CharField(choices=sections, max_length=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_single", kwargs={"pk": self.pk})


class Subject(models.Model):
    subject_code = models.CharField(
        max_length=10, unique=True, blank=False, null=False, primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subject_single", kwargs={"pk": self.pk})


class Teacher(models.Model):
    ssn = models.CharField(max_length=10, blank=False,
                           null=False, primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=50)
    phone = models.CharField(
        max_length=10, blank=False, null=False, unique=True)
    address = models.TextField()
    email = models.EmailField(unique=True, blank=False, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher_single", kwargs={"pk": self.pk})
