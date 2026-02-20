from django.contrib.auth.forms import UserCreationForm
from .models import User

class Userform(UserCreationForm):
    class Meta:
        model = User
        #password1 and password2 are required for user creation form
        fields = ['username', 'email','first_name','last_name','role','password1', 'password2']