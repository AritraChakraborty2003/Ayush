from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request,"dashboard.html")
def index(request):
    return render(request,"main.html")
def Login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid username or password")

    return render(request,"login.html")
def Signup(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(uname,email,password)
        user.save()
        return redirect("login")
    return render(request,"signup.html")

def logout(request):
    logouts(request)
    return redirect("main")