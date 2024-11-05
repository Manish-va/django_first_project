#department model.py
from datetime import timezone
from django.db import models
from django.utils import timezone

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_active_departments(self):
        return self.get_queryset().filter(is_active=True)
    
    def get_inactive_departments(self):
        return self.get_queryset().filter(is_active=False)
    

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    # Unique ID for each department, automatically incremented
    department_id = models.AutoField(primary_key=True)
    #HOD, related to the Teacher model
    hod = models.ForeignKey('myapp.Teacher', on_delete=models.SET_NULL,null=True,blank=True)
    # Reference to the school that this department belongs to
    #school_id = models.ForeignKey('School.School', on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.department_id}: {self.department_name}"
    objects = models.Manager()
    active_objects = ActiveManager()