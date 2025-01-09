from django.shortcuts import redirect,render


# Importing the built-in Django form for creating new user accounts.
# The line from django.contrib.auth.forms import UserCreationForm imports the UserCreationForm class from Django's authentication module,
#  allowing it to be used for creating new user accounts in the project.


#  from django.contrib.auth.forms import UserCreationForm             previous code   without emaifield    
from django.contrib import messages
from .forms import RegisterForm    # register form is created because there was no email field in usercreationform . So , to add email
#  field in our form , we create it by inheriting usercreationform class in our registerform class  
def register(request):
# When request method is post then if part is executed 
# In ' if ' block when request is post then UserCreationform is assign with data to the form variable and then check if form is valid . If form
#  is valid then username is assign to the username variable and that username is used in message to display it in index page after we hit signup 
    
    if request.method == 'POST':
      #  form= UserCreationForm(request.POST)              previous code which donot contain emaifield
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created..')
            return redirect('index')
    else:
        # form = UserCreationForm()          previous code which donot contain emaifield
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})
        