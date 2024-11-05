from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DepartmentSerializer
from .models import School
from .serializers import SchoolSerializer

class SchoolView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolDetailView(APIView):
    def get(self, request, pk):
        try:
            school = School.objects.get(school_id=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

    def put(self, request, pk):
        try:
            school = School.objects.get(school_id=pk)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            school = School.objects.get(school_id=pk)
            school.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class SchoolDepartmentListView(APIView):
    def get(self, request, pk):
        try:
            # Fetch the school by its primary key
            school = School.objects.get(school_id=pk)
            # Get the departments related to this school
            departments = school.departments.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ActiveSchoolView(APIView):
    def get(self, request):
        # Retrieve all active schools.
        active_schools = School.active_objects.filter(is_active=True)
        serializer = SchoolSerializer(active_schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        updated_count = School.objects.filter(school_id=pk).update(is_active=True)
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Fetch and return the updated school details
        updated_school = School.objects.filter(school_id=pk).first()
        if updated_school:
            serializer = SchoolSerializer(updated_school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class InactiveSchoolView(APIView):
    def get(self, request):
        # Retrieve all inactive schools.
        inactive_schools = School.objects.filter(is_active=False)
        serializer = SchoolSerializer(inactive_schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        # Inactivate a school by ID.
        updated_count = School.objects.filter(school_id=pk).update(is_active=False)
        if updated_count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Fetch and return the updated school details
        updated_school = School.objects.filter(school_id=pk).first()
        if updated_school:
            serializer = SchoolSerializer(updated_school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
