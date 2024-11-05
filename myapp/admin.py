from django.contrib import admin
from .models import Teacher, Student  


class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no','name','total','percentage','employee_id','department_id','school_id', 'is_active')  # Fields to be displayed in the list view

admin.site.register(Student,StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    """
    This class defines the configuration for the School model in the Django admin interface.
    It specifies the fields to be displayed in the list view and the fields to be used for filtering.
    """
    list_display = ('name','employee_id','department_id','performance', 'school_id','is_active')  # Fields to be displayed in the list view

admin.site.register(Teacher,TeacherAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('updated_on','created_on','is_admin','is_active')  # Fields to be displayed in the list view


