from django.shortcuts import render,redirect
from .models import Todo
from django.http import HttpResponse

# Create your views here.
def todo_list(request):
        todo=Todo.objects.order_by("-date_created")
        context={"todo":todo}
        return render(request,"home/index.html",context)

def todo_create(request):
        if request.method=="POST":
                title=request.POST.get("title")
                descp=request.POST.get("descp")
                todo=Todo.objects.create(title=title,description=descp,created_by=request.user)
                todo=Todo.objects.all().order_by("-date_created")
                context={"todo":todo}
                return render(request,"home/index.html",context)
        
def complete_todo(request,id):
        try:
            todo=Todo.objects.get(id=id)
            if todo.created_by == request.user:
                  todo.is_completed=True
                  todo.save()
            else:
                  return HttpResponse("You are not authorized to complete this todo")
        except:
               return HttpResponse("not found")
        return redirect("todo_list")


def delete_todo(request,id):
        try:
            todo=Todo.objects.get(id=id)
            if todo.created_by == request.user:
                  todo.is_completed=True
                  todo.delete()
            else:
                  return HttpResponse("You are not authorized to delete this todo")

        except:
               return HttpResponse("not found Invalid")
        return redirect("todo_list")

def update_todo(request,id):
        try:
            todo=Todo.objects.get(id=id)
            if todo.created_by != request.user:
                  return HttpResponse("You are not authorized to update this todo")
            
        except:
               return HttpResponse("not found Invalid")
        if(request.method=="POST"):
           title=request.POST.get("title")
           descp=request.POST.get("descp")
           todo.title=title
           todo.description=descp
           todo.save()
           return redirect("todo_list")
        return render(request,"home/update.html",{"todo":todo})
        
        
        
        
        
        

        

        
       
       

