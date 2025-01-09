from django import forms
from django.contrib.auth.models import User   #  importing user model
from django.contrib.auth.forms import UserCreationForm  #  importing usercreation form

class RegisterForm(UserCreationForm):    #  inheriting user creationform to our own form i.e registerform
    email = forms.EmailField()         #adding additional field

    class Meta:                        #defining metaclass for this paticular class
                                       #meta class mean the class which provides the information about the above class itself
        model = User
        fields = ['username','email','password1','password2']