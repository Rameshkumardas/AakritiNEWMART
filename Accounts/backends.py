from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class LoginWithEmailBackend(ModelBackend):
    def authenticate(self, request, username, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            if username:
                user = UserModel.objects.get(email=username)
                return user
            else:
                return username
        except UserModel.DoesNotExist:
            return username

        