from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models  import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    
    return render( request ,'kabianga/base.html')

 

def signupuser(request):
    if request.method =='GET':
      return render(request,'kabianga/signupuser.html',{'form':UserCreationForm()})

    else:
        #Create a new user
        if request.POST['password1'] == request.POST['password2']:
           try:  
            user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return  redirect('home')
            
            
           except IntegrityError:  
                return render(request,'kabianga/signupuser.html',{'form':UserCreationForm(), 'error':'That userSname has already been taken,Please choose a new username'})

        else:
            return render(request,'kabianga/signupuser.html',{'form':UserCreationForm(), 'error':'passwords did not match'})
def loginuser(request):
    
    if request.method =='GET':
      return render(request,'kabianga/loginuser.html',{'form':AuthenticationForm()})

    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password']) 
       if user is None:
                 return render(request,'kabianga/loginuser.html',{'form':AuthenticationForm(), 'error': 'username and password did not match'})

       else:
            login(request, user)
            return  redirect('home')   
    
@login_required            
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    