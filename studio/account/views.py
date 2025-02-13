from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.

from .models import User

def login(request):
    if request.method=="POST":
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        if email and password:
            user=authenticate(request,email=email,password=password)
            print("in")
            if user is not None:
                auth_login(request,user)

                print('User',user)

                print(request.user)
                print(request.user.is_authenticated)

                return redirect('/')
            else:
                print("Invalid email or password")

    return render(request,'account/login.html')

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')

        if name and email and password1 and password2:
            user=User.objects.create_user(name,email,password1)
            print('User created:',user)

            return redirect('/login/')
        else:
            print("something went wrong")
    else:
        print('Jsut show the form!')
    return render(request,'account/signup.html')