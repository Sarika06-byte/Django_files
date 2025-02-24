from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import CreateAccount
from django.contrib.auth import authenticate,login as login_acc,logout as logout_acc

# Create your views here.

def profile(request):
  user=User.objects.all()

def create(request):
  if request.method=="POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    img1=request.FILES.get("img1")
    img2=request.FILES.get("img2")
    location=request.POST.get("location")
    bio=request.POST.get("bio")
    dob=request.POST.get("dob")
    if username in User.objects.values_list("username",flat=True):
        return HttpResponse("username already exist")
    user=User.objects.create_user(username=username)
    user.set_password(password)
    user.save()
    user_account=CreateAccount.objects.create(
      user = user,
      date_of_birth=dob,
      location=location,
      bio=bio,
      profile_pictures=img1,
      cover_image=img2,
    )
    return redirect("login")
  
  return render(request,"accounts/register.html")

def login(request):
  if request.method=="POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login_acc(request,user)
      return redirect("accounts/profile.html")
    else:
       return HttpResponse("username not exist")
  return render(request,"accounts/login.html")

def logout(request):
  login_acc(request)
  return redirect("login")


