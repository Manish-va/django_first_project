from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    """
    This class defines the configuration for the Department model in the Django admin interface.
    It specifies the fields to be displayed in the list view and the fields to be used for filtering.
    """
    list_display = ('department_name','department_id','hod','is_active')  # Fields to be displayed in the list view

admin.site.register(Department,DepartmentAdmin)


   
