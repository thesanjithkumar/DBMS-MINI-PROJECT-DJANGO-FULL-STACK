from django import forms
from django.db.models import fields
from . import models


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'dept_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Id', 'required': 'required', }),
            'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name', 'required': 'required', }),
        }


class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = "__all__"
        widgets = {
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usn', 'required': 'required', }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xx-xxxx-xxxx', 'required': 'required', }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com', 'required': 'required', }),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'required': 'required', }),
            'dept': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required', }),
            'sem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Semester', 'required': 'required', }),
            'section': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section', 'required': 'required', }),
        }


class SubjectForm(forms.ModelForm):

    class Meta:
        model = models.Subject
        fields = "__all__"
        widgets = {
            'subject_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Code', 'required': 'required', }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name', 'required': 'required', }),
            'dept': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required', }),
        }


class TeacherForm(forms.ModelForm):

    class Meta:
        model = models.Teacher
        fields = "__all__"
        widgets = {
            'ssn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usn', 'required': 'required', }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xx-xxxx-xxxx', 'required': 'required', }),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com', 'required': 'required', }),
            'email': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'required': 'required', }),
            'dept': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required', }),
        }
