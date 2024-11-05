from rest_framework import serializers
from .models import Student,Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        # fields = ['name', 'employee_id', 'performance', 'created_on', 'updated_on','department_id',]  # Inclde 'name' and 'employee_id' fields
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset = Teacher.objects.all())
    class Meta:
        model = Student
        # fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'total', 'percentage','employee_id', 'department_id', 'created_on', 'updated_on']
        fields = '__all__'