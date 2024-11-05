from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print(f"Authenticating user: {username}")  # Debugging log

        try:
            user = get_user_model().objects.get(username=username)
            print(f"User found: {user.username}")  # Debugging log

            if check_password(password, user.password):
                print(f"Password match for user: {user.username}")  # Debugging log
                return user
            else:
                print(f"Password mismatch for user: {user.username}")  # Debugging log
        except get_user_model().DoesNotExist:
            print("User not found")  # Debugging log
            return None
        
        return None
