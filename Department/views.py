
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department
from .serializers import DepartmentSerializer



class DepartmentView(APIView):
    def get(self, request):
        # Get all department records from the database.
        departments = Department.objects.all()
        # Serialize the department records.
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new department based on the data sent in the request.
        serializer = DepartmentSerializer(data=request.data)
        # Validate the data.
        if serializer.is_valid():
            # Save the new department record.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DepartmentByIdView(APIView):
    def get(self, request, department_id):
        # Try to get the department using the provided ID.
        try:
            department = Department.objects.get(department_id=department_id)  
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, department_id):
        # Try to get the department by ID for updating.
        try:
            department = Department.objects.get(department_id=department_id)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, department_id):
            # delete the department using the provided ID.
            dept = Department.objects.get(department_id=department_id)
            dept.delete()  
            return Response(status=status.HTTP_204_NO_CONTENT)

class ActiveDepartmentView(APIView):
    def get(self, request):
        #Retrieve all active departments.
        active_departments = Department.active_objects.filter(is_active=True)
        serializer = DepartmentSerializer(active_departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, department_id):
        # Activate a department by ID.
        updated_count = Department.objects.filter(department_id=department_id).update(is_active=True)
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_200_OK)
        
class InactiveDepartmentView(APIView):
    def get(self, request):
        #Retrieve all inactive departments.
        inactive_departments = Department.active_objects.filter(is_active=False)
        serializer = DepartmentSerializer(inactive_departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, department_id):
        # Inactivate a department by ID.
        updated_count = Department.objects.filter(department_id=department_id).update(is_active=False)
    
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Fetch and return the updated department details
        updated_department = Department.objects.filter(department_id=department_id).first()
        if updated_department:
            serializer = DepartmentSerializer(updated_department)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
