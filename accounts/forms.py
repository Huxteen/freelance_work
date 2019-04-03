from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    username = None

    class Meta:
        model = User
        fields = (
            'email', 
            'password1', 
            'password2', 
        )

  
