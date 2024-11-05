# from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
from .logic import (
    get_pass_students,
    get_fail_students,
    get_top_students,
    get_students_below_average,
    get_students_above_average,
    calculate_totals_and_percentage,
)
from .logic2 import teacher_performance

class StudentView(APIView):
    def get(self, request):
        # Retrieve all student records from the database
        students = Student.objects.all()
        # Serialize the student records
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Create a new student using the data from the request
        serializer = StudentSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # Save the new student record
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentByIdView(APIView):
    # Handle requests related to a specific student by their ID (roll number)
    def get(self, request, pk):
        try:
            # Retrieve a specific student based on roll number (pk)
            student = Student.objects.get(roll_no=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            student = Student.objects.get(roll_no=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Create a serializer for the existing student with the updated data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            # Save the updated student record
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            student = Student.objects.get(roll_no=pk)
            # Delete the student record
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# View to retrieve a specific student by roll number (using generics)
class StudentDetailView(generics.RetrieveAPIView):
    # Specify the queryset to retrieve student records
    queryset = Student.objects.all()
    # Specify the serializer class to use for serialization
    serializer_class = StudentSerializer
    # Specify the field used to look up student records (by roll number)
    lookup_field = 'roll_no'

class CalculatePercentageView(APIView):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            total, percentage = calculate_totals_and_percentage(student)
            return Response({
                'total': total,
                'percentage': percentage
            }, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PassStudentsView(APIView):
    def get(self, request):
        # Retrieve students who have passed
        passing_students = get_pass_students(cutoff=40)
        serializer = StudentSerializer(passing_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FailStudentsView(APIView):
    def get(self, request):
        # Retrieve students who have failed
        failing_students = get_fail_students(cutoff=40)
        serializer = StudentSerializer(failing_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# View to get the top students based on total marks
class TopStudentsView(APIView):
    def get(self, request):
        top_students = get_top_students()
        serializer = StudentSerializer(top_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View to get students below average
class StudentsBelowAverageView(APIView):
    def get(self, request):
        students = get_students_below_average()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View to get students above average
class StudentsAboveAverageView(APIView):
    def get(self, request):
        students = get_students_above_average()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# View for students by department
class StudentsByDepartmentView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Student.objects.filter(department_id=department_id)
    
class ActiveStudentView(APIView):
    def get(self, request):
        #Retrieve all active students.
        active_students = Student.active.filter(is_active=True)
        serializer = StudentSerializer(active_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, roll_no):
        updated_count= Student.objects.filter(roll_no=roll_no).update(is_active=True)
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        updated_student = Student.objects.get(roll_no=roll_no).first()
        if updated_student:
            serializer = StudentSerializer(updated_student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class InactiveStudentView(APIView):
    def get(self, request):
        #Retrieve all inactive students.
        inactive_students = Student.objects.filter(is_active=False)
        serializer = StudentSerializer(inactive_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, roll_no):
        # inactivate a student by roll number.
        try:
            student = Student.objects.get(roll_no=roll_no)
            student.is_active = False
            student.save()
            return Response(status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    


class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            # Automatically assign the school_id based on department_id
            if teacher.department_id and teacher.department_id.school_id:
                teacher.school_id = teacher.department_id.school_id
                teacher.save(update_fields=['school_id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherByIdView(APIView):
    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(employee_id=pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(employee_id=pk)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            teacher = Teacher.objects.get(employee_id=pk)
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TeacherPerformanceView(APIView):
    def get(self, request):
        # Get performance metrics for each teacher.
        teachers = Teacher.objects.all()
        performance_data = []

        for teacher in teachers:
            # Retrieve students associated with the current teacher
            student_data = Student.objects.filter(employee_id=teacher.employee_id)
            # Calculate performance metrics for the students of this teacher
            performance = teacher_performance(student_data)
            # Append the performance metrics and teacher info to the list
            performance_data.append({
                'teacher_employee_id': teacher.employee_id,
                'department_id': teacher.department_id.department_name if teacher.department_id else "N/A",
                'teacher_name': teacher.name,
                'performance_percentage': performance['performance_percentage'],
                'school_id': teacher.school_id.school_name if teacher.school_id else "-",
                'total_students': performance['total_students'],
                'total_passed': performance['total_passed'],
                'created_on': teacher.created_on, 
                'updated_on': teacher.updated_on 
            })
        return Response(performance_data, status=status.HTTP_200_OK)

class ActiveTeacherView(APIView):
    def get(self, request, pk=None):
        # Retrieve all active teachers.
        if pk is not None:
            try:
                teacher = Teacher.objects.get(employee_id=pk)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        active_teachers = Teacher.active.filter(is_active=True)
        serializer = TeacherSerializer(active_teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        # Activate a teacher by employee ID.
        updated_count = Teacher.objects.filter(employee_id=pk).update(is_active=True)

        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        updated_teacher = Teacher.objects.filter(employee_id=pk).first()
        if updated_teacher:
            serializer=TeacherSerializer(updated_teacher)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class InactiveTeacherView(APIView):
    def get(self, request, pk=None):
        # Retrieve all inactive teachers or a specific inactive teacher.
        if pk is not None:
            try:
                teacher = Teacher.objects.get(employee_id=pk, is_active=False)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        inactive_teachers = Teacher.objects.filter(is_active=False)
        serializer = TeacherSerializer(inactive_teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        # Inactivate a teacher by employee ID.
        updated_count = Teacher.objects.filter(employee_id=pk).update(is_active=False)
    
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        updated_teacher = Teacher.objects.filter(employee_id=pk).first()
        if updated_teacher:
            serializer=TeacherSerializer(updated_teacher)
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_200_OK)

