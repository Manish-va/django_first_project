# from django.contrib import admin
# from .models import School 

# class SchoolAdmin(admin.ModelAdmin):
#     """
#     This class defines the configuration for the School model in the Django admin interface.
#     It specifies the fields to be displayed in the list view and the fields to be used for filtering.
#     """
#     list_display = ('school_name','school_id','departments','location','is_active')  # Fields to be displayed in the list view

# admin.site.register(School,SchoolAdmin)

from django.contrib import admin
from .models import School 

class SchoolAdmin(admin.ModelAdmin):
    """
    This class defines the configuration for the School model in the Django admin interface.
    It specifies the fields to be displayed in the list view and the fields to be used for filtering.
    """
    list_display = ('school_name', 'school_id', 'get_departments', 'location', 'is_active')  # Use custom method

    def get_departments(self, obj):
        return ", ".join([dept.department_name for dept in obj.departments.all()])  # Assuming departments has a department_name field
    get_departments.short_description = 'Departments'  # Set column name in admin

admin.site.register(School, SchoolAdmin)
