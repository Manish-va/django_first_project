
from Department.models import Department  
from School.models import School
from myapp.models import Teacher, Student

def run():
    # Fetch all schools to update their departments if necessary
    schools = School.objects.all()
    
    for school in schools:
        try:
            # Fetch all departments related to this school
            associated_departments = school.departments.all()
            print(f'Updating school {school.school_name} with its departments')
            
            # Fetch teachers and departments are linked to the school
            teachers = Teacher.objects.filter(school_id=school)
            for teacher in teachers:
                if teacher.department_id and teacher.department_id not in associated_departments:
                    school.departments.add(teacher.department_id)  # Add department if not already present
                    print(f'Added department {teacher.department_id.department_name} to school {school.school_name}.')
            
            # removing any departments that no longer have teachers
            for department in associated_departments:
                if not Teacher.objects.filter(department_id=department, school_id=school).exists():
                    school.departments.remove(department)
                    print(f'Removed department {department.department_name} from school {school.school_name} (no teachers associated).')

        except Exception as e:
            print(f'Error updating school {school.school_name}: {e}')

    # Fetch all students and update their department and school associations
    students = Student.objects.all()

    for student in students:
        try:
            # Get the teacher associated with the student
            teacher = student.employee_id
            if teacher and teacher.department_id:
                student.department_id = teacher.department_id
                student.school_id = teacher.school_id
                student.save() 
                print(f'Successfully updated student {student.roll_no}: '
                      f'Department to {teacher.department_id.department_name} and School to {teacher.school_id.school_name}.')
            else:
                print(f'Student {student.roll_no} has no associated teacher or department.')
        except Exception as e:
            print(f'Error updating student {student.roll_no}: {e}')

if __name__ == '__main__':
    run()
