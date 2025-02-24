from django.urls import path
from .views import *

urlpatterns = [
 path("create/",create_account,name="create"),
 path("login/",login_account,name="login"),
  path("logout/",logout_account,name="logout"),

]