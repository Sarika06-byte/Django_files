from django.urls import path
from .views import *
urlpatterns =[
    
    #  path("app"),
    # path('',views.homePage,name='home')
    # path('',views.add,name='add')
       path('app/add',add),
       path('app/div',div),
       path('app/mul',mul),
       path('app/sub',sub),
       path('app/mod',mod),    
        path('app/select',select),       
       path("",home),
        # path("",homePage),
   
]