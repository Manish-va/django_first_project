from datetime import timezone
from django.db import models
from django.utils import timezone

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_active_schools(self):
        return self.get_queryset().filter(is_active=True)
    
    def get_inactive_schools(self):
        return self.get_queryset().filter(is_active=False)
    

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_id = models.AutoField(primary_key=True,)
    location = models.CharField(max_length=100)
    departments = models.ManyToManyField('Department.Department', related_name='schools')

    
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)


    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.school_id} : {self.school_name}"
    

    objects = models.Manager()
    active_objects = ActiveManager()