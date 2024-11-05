from myapp.models import Teacher
from user.models import Custom_User
from django.utils import timezone
from django.db import IntegrityError
from django.utils.crypto import get_random_string

def create_users_for_teachers():
    # Filter for active teachers
    teachers = Teacher.objects.filter(is_active=True)  

    for teacher in teachers:
        # Generate a username based on the teacher's name and employee ID
        base_username = f"{teacher.name.lower().replace(' ', '_')}_{teacher.employee_id}"
        username = base_username
        
        # Check if the username already exists. If so, append a random string to make it unique.
        while Custom_User.objects.filter(username=username).exists():
            # Append a random string of length 4 to the base username
            username = f"{base_username}_{get_random_string(4)}"
        
        # Assign the role based on whether the teacher is an HOD or not
        if teacher.department_id and teacher.department_id.hod == teacher:
            role = 'HOD' 
        else:
            role = 'staff'  
        
        # Split the teacher's name into first name and last name
        name_parts = teacher.name.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

        # Automatically generate the email username@school.com
        email = f"{username}@{teacher.school_id.school_name.lower().replace(' ', '_')}.com"  # Using school name in domain
        
        # Extract performance from the teacher model
        performance = teacher.performance if hasattr(teacher, 'performance') else None

        try:
            # Create new Custom_User instance using teacher data
            user = Custom_User(
                username=username,
                first_name=first_name, 
                last_name=last_name,   
                email=email,            
                employee_id=teacher.employee_id,
                role=role, 
                department_id=teacher.department_id,
                school_id=teacher.school_id,
                last_login=timezone.now(),  
                performance=performance,  # Include performance data here
            )

            # Save the user (this will trigger the password generation in the save method)
            user.save()

            print(f"Created user: {user.username} with role {user.role}, performance {user.performance} and a generated password.")

        except IntegrityError as e:
            print(f"Error creating user for {teacher.name}: {e}")

def run():
    print("Starting user creation for teachers...")
    create_users_for_teachers()
    print("User creation process completed.")

if __name__ == "__main__":
    run()
