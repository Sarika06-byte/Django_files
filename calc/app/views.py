from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    return HttpResponse("hello")


def add(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    return HttpResponse("ADDITION : "+str(a+b))


def div(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    return HttpResponse("DIVISION : "+str(a/b))


def mul(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    return HttpResponse("MULTIPLE : "+str(a*b))


def sub(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    return HttpResponse("SUBTRACT : "+str(a-b))


def mod(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    return HttpResponse("MODULO : "+str(a%b))
   
def home(request):
    return render(request,"app/home.html")

def select(request):
    a=int(request.POST.get('n1'))
    b=int(request.POST.get('n2'))
    op=int(request.POST.get('op'))
    res=0
    if(op==1):
        # return HttpResponse("ADDITION : "+str(a+b))
          res=a+b
    
    elif(op==2):
        # return HttpResponse("SUBTRACT : "+str(a-b))
          res=a-b
    elif(op==3):
        # return HttpResponse("MULTIPLE : "+str(a*b))
        res=a*b
    elif(op==4):
        # return HttpResponse("DIVISION : "+str(a/b))
        res=a/b
    elif(op==5):
        # return HttpResponse("MODULO : "+str(a%b))
        res=a%b
    else:
        return HttpResponse("WRONG INPUT ")
        exit
    context={'res':res}
    return render(request,"app/res.html",context)

    

