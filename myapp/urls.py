from django.urls import path
from .views import (
    ActiveStudentView,
    ActiveTeacherView,
    CalculatePercentageView,
    InactiveStudentView,
    InactiveTeacherView,
    StudentByIdView,
    PassStudentsView,
    FailStudentsView,
    StudentDetailView,
    StudentView,
    StudentsByDepartmentView,
    TeacherByIdView,
    TopStudentsView,
    StudentsBelowAverageView,
    StudentsAboveAverageView,
    TeacherPerformanceView,
    TeacherView,

)

urlpatterns = [
    path('students/', StudentView.as_view(), name='student-list-create'), 
    path('students/<int:pk>/', StudentByIdView.as_view(), name='student-detail'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:student_id>/percentage/', CalculatePercentageView.as_view(), name='calculate-percentage'),
    path('students/passing/', PassStudentsView.as_view(), name='passing-students'),
    path('students/failing/', FailStudentsView.as_view(), name='failing-students'),
    path('students/top/', TopStudentsView.as_view(), name='top-students'),
    path('students/below-average/', StudentsBelowAverageView.as_view(), name='students-below-average'),
    path('students/above-average/', StudentsAboveAverageView.as_view(), name='students-above-average'),
    path('students/department/<int:department_id>/', StudentsByDepartmentView.as_view(), name='students-by-department'),
    path('teachers/performance/', TeacherPerformanceView.as_view(), name='teacher-performance'),
    path('students/active/', ActiveStudentView.as_view(), name='active-student-list'),
    path('students/inactive/', InactiveStudentView.as_view(), name='inactive-student-list'),
    path('teachers/', TeacherView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherByIdView.as_view(), name='teacher-detail'),
    path('teachers/active/', ActiveTeacherView.as_view(), name='active-teacher-list'),
    path('teachers/inactive/', InactiveTeacherView.as_view(), name='inactive-teacher-list'),
    path('teachers/active/<int:pk>/', ActiveTeacherView.as_view(), name='activate-teacher'),
    path('teachers/inactive/<int:pk>/', InactiveTeacherView.as_view(), name='inactivate-teacher'),
]