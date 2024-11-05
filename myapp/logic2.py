from django.db.models import Q

def teacher_performance(student_data):
    #Calculate performance metrics for a given queryset of students
    # If there are no students, return zero metrics
    if student_data is None or student_data.count() == 0:
        return {
            'total_students': 0,
            'total_passed': 0,
            #'total_failed': 0,
            'performance_percentage': 0
        }
    # Count the total number of students
    total_students = student_data.count()
     # Count how many students have a total score of 40 or more (passed)
    total_passed = student_data.filter(total__gte=40).count()
    # Calculate the performance percentage of students who passed
    performance_percentage = (total_passed / total_students * 100) if total_students > 0 else 0
    # Return a dictionary with performance metrics of students
    return {
        'total_students': total_students,
        'total_passed': total_passed,
        'performance_percentage': performance_percentage
    }
