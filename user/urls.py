from django.urls import path
from .views import UserView, UserDetailView, LoginView

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),  # List all users and create a new user
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),  # View a specific user by pk
    path('login/', LoginView.as_view(), name='login')
]
