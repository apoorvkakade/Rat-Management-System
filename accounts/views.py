from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=='GET':
        return render(request,'register.html')

    elif request.method=='POST':

        username=request.POST['username']
        firstname=str(request.POST['first_name'])
        firstname.strip()
        lastname=str(request.POST['last_name'])
        lastname.strip()
        password=request.POST['password1']
        email=request.POST['email']
        if User.objects.filter(username=username).exists(): #username is already taken
            return redirect('register')
        if User.objects.filter(email=email).exists():
            return redirect('register') #email is already taken
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
            user.save()
            return redirect('login')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print("Login success")
            auth.login(request,user)
            return redirect('home')

        else:
            print("Login unsuccessful")
            return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')





