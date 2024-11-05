from django.utils import timezone 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_active_schools(self):
        return self.get_queryset().filter(is_active=True)
    
    def get_inactive_schools(self):
        return self.get_queryset().filter(is_active=False)


class Custom_User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=16)
    employee_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    performance = models.FloatField(blank=True, editable=False, null=True)
    department_id = models.ForeignKey('Department.Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    school_id = models.ForeignKey('School.School', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'


    objects = models.Manager()
    active_objects = ActiveManager()











