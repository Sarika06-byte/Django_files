from django.urls import path
from .views import *

urlpatterns = [
   
    path("profile/",profile,name="profile"),
    path("create/",create,name="create"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
]