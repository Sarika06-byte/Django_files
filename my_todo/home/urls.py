
from django.urls import path
from .views import *

urlpatterns = [
 path("",todo_list,name="todo_list"),
 path("create/",todo_create,name="create"),
 path("complete/<int:id>",complete_todo,name="complete"),
  path("delete/<int:id>",delete_todo,name="delete"),
  path("update/<int:id>",update_todo,name="update"),
]