from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import Custom_User
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password



class LoginView(APIView):
    def post(self, request):
        # Extract username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if both username and password are provided
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Query the Custom_User model for the user by username
        try:
            user = Custom_User.objects.filter(username=username).first() # Get user by username
        except Custom_User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Verify the password using check_password (it compares the plain-text password with the hashed password)
        if check_password(password, user.password):
            # If the password matches, create or get the token for the user
            token, created = Token.objects.get_or_create(user=user)  # Pass the user object, not the username string
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# API View to manage Custom_User objects
class UserView(APIView):
    # Get all users
    def get(self, request):
        users = Custom_User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new user
    def post(self, request):
        # Deserialize the data and validate it
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Manually hash the password before saving the user
            password = serializer.validated_data['password']
            hashed_password = make_password(password)  # Hash the password
            
            # Create the user object and save it with the hashed password
            user = Custom_User(username=serializer.validated_data['username'], password=hashed_password)
            user.save()
            
            # Return the response with the serialized data of the user (without password)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the serializer is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    # Update an existing user (by primary key)
    def put(self, request, pk):
        user = get_object_or_404(Custom_User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a user (by primary key)
    def delete(self, request, pk):
        user = get_object_or_404(Custom_User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Detail view for individual users (optional but recommended for clarity)
class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(Custom_User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
