from typing import List
from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView, DetailView, ListView, CreateView, DeleteView, UpdateView)
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
# Create your views here.


class HomePage(TemplateView):

    template_name = 'database/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept_count'] = models.Department.objects.all().count()
        context['student_count'] = models.Student.objects.all().count()
        context['subject_count'] = models.Subject.objects.all().count()
        context['teacher_count'] = models.Teacher.objects.all().count()

        return context

# department views


class DepartmentList(ListView):
    model = models.Department


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    redirect_field_name = 'database/department_detail.html'
    form_class = forms.DepartmentForm
    model = models.Department


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'user:login'
    redirect_field_name = 'database/department_detail.html'
    form_class = forms.DepartmentForm
    model = models.Department


class DepartmentDetailView(DetailView):
    model = models.Department


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Department
    success_url = reverse_lazy('depts')


# department views

# student views
class StudentList(ListView):
    model = models.Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    redirect_field_name = 'database/student_detail.html'
    form_class = forms.StudentForm
    model = models.Student


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'user:login'
    redirect_field_name = 'database/department_detail.html'
    form_class = forms.StudentForm
    model = models.Student


class StudentDetailView(DetailView):
    model = models.Student


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Student
    success_url = reverse_lazy('students')

# student views

# subjedt views


class SubjectList(ListView):
    model = models.Subject


class SubjectCreateView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    redirect_field_name = 'database/subject_detail.html'
    form_class = forms.SubjectForm
    model = models.Subject


class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'user:login'
    redirect_field_name = 'database/subject_detail.html'
    form_class = forms.SubjectForm
    model = models.Subject


class SubjectDetailView(DetailView):
    model = models.Subject


class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Subject
    success_url = reverse_lazy('subjects')

# subject views

# teacher views


class TeacherList(ListView):
    model = models.Teacher


class TeacherCreateView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    redirect_field_name = 'database/teacher_detail.html'
    form_class = forms.TeacherForm
    model = models.Teacher


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'user:login'
    redirect_field_name = 'database/teacher_detail.html'
    form_class = forms.TeacherForm
    model = models.Teacher


class TeacherDetailView(DetailView):
    model = models.Teacher


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Teacher
    success_url = reverse_lazy('teachers')

# teachers view
