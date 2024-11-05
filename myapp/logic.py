from .models import Student
from django.db.models import Q,Avg

def calculate_totals_and_percentage(student, max_marks=150):
    total = student.total 
    percentage = (total / max_marks) * 100 if max_marks > 0 else 0  
    return total, percentage
    
def get_pass_students(cutoff=40):
    return Student.objects.filter(total__gte=cutoff)


def get_fail_students(cutoff=40):
    return Student.objects.filter(total__lt=cutoff)



def get_top_students(limit=5):
    #Get top students based on total marks
    return Student.objects.order_by('-total')[:limit]

def get_students_below_average():
    #Get students whose total marks are below average."""
    average = Student.objects.aggregate(Avg('total'))['total__avg'] or 0
    return Student.objects.filter(total__lt=average)

def get_students_above_average():
    #Get students whose total marks are above average
    average = Student.objects.aggregate(Avg('total'))['total__avg'] or 0
    return Student.objects.filter(total__gt=average)

def get_students_failing_subject(subject, cutoff=20):
    #Get students who failed a specific subject
    return Student.objects.filter(**{f"{subject}__lt": cutoff})

def get_students_passing_subject(subject, cutoff=20):
    #Get students who passed a specific subject
    return Student.objects.filter(**{f"{subject}__gte": cutoff})
