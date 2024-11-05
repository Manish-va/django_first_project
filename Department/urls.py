from django.urls import path
from .views import ActiveDepartmentView, DepartmentView, DepartmentByIdView, InactiveDepartmentView

urlpatterns = [
    path('', DepartmentView.as_view(), name='department-list'),  
    path('departments/<int:department_id>/', DepartmentByIdView.as_view(), name='department-detail'),
    path('departments/active/', ActiveDepartmentView.as_view(), name='active-departments'),
    path('departments/active/<int:department_id>/', ActiveDepartmentView.as_view(), name='activate-department'),
    path('departments/inactive/', InactiveDepartmentView.as_view(), name='inactive-departments'),
    path('departments/inactive/<int:department_id>/', InactiveDepartmentView.as_view(), name='deactivate-department'),
]