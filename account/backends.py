from django.contrib.auth.backends import BaseBackend
from account.models import User

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        print(0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        print(user.check_password(password))

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None