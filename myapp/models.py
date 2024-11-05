from datetime import timezone
from django.db import models
from myapp.logic2 import teacher_performance
from django.utils import timezone
import random


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_active_teacher(self):
        return self.get_queryset().filter(is_active=True)
    
    def get_inactive_teacher(self):
        return self.get_queryset().filter(is_active=False)
    

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    # Unique ID for each teacher, automatically incremented
    employee_id = models.AutoField(primary_key=True)
    # Performance score of the teacher
    performance = models.FloatField(blank=True, editable=False, null=True)
    # Reference to the department this teacher and school belongs to
    department_id = models.ForeignKey('Department.Department', on_delete=models.DO_NOTHING, null=True,blank=True)
    school_id = models.ForeignKey('School.School', on_delete=models.DO_NOTHING, null=True, blank=True)
    # Timestamp for when the teacher was created
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    # Timestamp for when the teacher was last updated
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    objects = models.Manager()
    active = ActiveManager()
    def save(self, *args, **kwargs):
        # Update school_id based on department_id only if department_id is assigned
        if self.department_id:
            # Find the first school associated with this department
            school = self.department_id.schools.first()  # Assuming a department can have multiple schools
            if school:
                self.school_id = school  # Set the school_id from the department

        super().save(*args, **kwargs)  # Save the teacher instance
        self.update_performance()  # Update performance after saving 

    def update_performance(self):
        # Get the students associated with this teacher
        student_data = Student.objects.filter(employee_id=self)
        if student_data.exists():
            # Calculate the performance based on students
            performance_data = teacher_performance(student_data)
            self.performance = performance_data['performance_percentage']
            # Save only the performance field to avoid recursion
            # self.save(update_fields=['performance'])

            # Update the performance field in the database
            Teacher.objects.filter(employee_id=self.employee_id).update(performance=self.performance)

    def __str__(self):
        performance_display = f"{self.performance:.1f}" if self.performance is not None else 0.0
        return f"{self.employee_id} : {self.name}"


    

class Student(models.Model):
    name = models.CharField(max_length=50)
    # Unique ID for each student
    roll_no = models.AutoField(primary_key=True)
    # Marks in different subjects
    # chemistry = models.IntegerField(default=0)
    # physics = models.IntegerField(default=0)
    # maths = models.IntegerField(default=0)
    total = models.IntegerField(editable=True)
    percentage = models.FloatField(editable=True)
    # Reference to the teacher this student is linked to
    employee_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True, blank=True)
    # Reference to the department this student belongs to
    department_id = models.ForeignKey('Department.Department', on_delete=models.SET_NULL, null=True,blank=True)
    school_id = models.ForeignKey('School.School', on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
     
    objects = models.Manager()
    active = ActiveManager()

    def save(self, *args, **kwargs):

        if self.employee_id:
            self.employee_id.update_performance()  


        if self.total is None:
            self.total = random.uniform(20,150)

        if self.percentage is None:
            self.percentage = (self.total/150)*100

        super(Student, self).save(*args, **kwargs)  
        

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no}, Total: {self.total})"

    