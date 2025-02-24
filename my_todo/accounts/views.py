from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as login_acc,authenticate,logout as logout_acc
from django.http import HttpResponse

# Create your views here.

def create_account(request):
      if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        if email in User.objects.values_list("email",flat=True):
            return HttpResponse("Email already exist!")
        if username in User.objects.values_list("username",flat=True):
            return HttpResponse("Username already exist!")
        user=User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect("login")
      return render(request,"accounts/create_accounts.html")




def login_account(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login_acc(request,user)
            return redirect("todo_list")
        else:
            return HttpResponse("Invalid credentials")
        
    return render(request,"accounts/login.html")



def logout_account(request):
    logout_acc(request)
    return redirect("login")
    
        
    
    


    