from django.urls import path
from .views import ActiveSchoolView, InactiveSchoolView, SchoolDepartmentListView, SchoolDetailView, SchoolView

urlpatterns = [
    path('', SchoolView.as_view(), name='school-list'),  
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'), 
    path('schools/active/', ActiveSchoolView.as_view(), name='active-school-list'),
    path('schools/active/<int:pk>/', SchoolDetailView.as_view(), name='active-school-detail'),
    path('schools/inactive/', InactiveSchoolView.as_view(), name='inactive-school-list'),
    path('schools/inactive/<int:pk>/', SchoolDetailView.as_view(), name='inactive-school-detail'),
    path('schools/<int:pk>/departments/', SchoolDepartmentListView.as_view(), name='school-departments'),
]
