from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    # dept urls
    path('depts/', views.DepartmentList.as_view(), name='depts'),
    path('dept/new/', views.DepartmentCreateView.as_view(), name='dept_new'),
    path('dept/<str:pk>/', views.DepartmentDetailView.as_view(), name='dept_single'),
    path('dept/<str:pk>/update/',
         views.DepartmentUpdateView.as_view(), name='dept_update'),
    path('dept/<str:pk>/delete/',
         views.DepartmentDeleteView.as_view(), name='dept_delete'),
    # dept urls
    # student urls
    path('students/', views.StudentList.as_view(), name='students'),
    path('student/new/', views.StudentCreateView.as_view(), name='student_new'),
    path('student/<str:pk>/', views.StudentDetailView.as_view(),
         name='student_single'),
    path('student/<str:pk>/update/',
         views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<str:pk>/delete/',
         views.StudentDeleteView.as_view(), name='student_delete'),
    # student urls
    # subject urls
    path('subjects/', views.SubjectList.as_view(), name='subjects'),
    path('subject/new/', views.SubjectCreateView.as_view(), name='subject_new'),
    path('subject/<str:pk>/', views.SubjectDetailView.as_view(),
         name="subject_single"),
    path('subject/<str:pk>/update/',
         views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<str:pk>/delete/',
         views.SubjectDeleteView.as_view(), name='subject_delete'),
    # subject urls
    path('teachers/', views.TeacherList.as_view(), name='teachers'),
    path('teacher/new/', views.TeacherCreateView.as_view(), name='teacher_new'),
    path("teacher/<str:pk>/", views.TeacherDetailView.as_view(),
         name="teacher_single"),
    path('teacher/<str:pk>/update/',
         views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<str:pk>/delete/',
         views.TeacherDeleteView.as_view(), name='teacher_delete'),
]
