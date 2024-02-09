# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']