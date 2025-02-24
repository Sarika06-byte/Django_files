from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CreateAccount(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,null=True)
    profile_pictures=models.ImageField(upload_to="profile_pictures/",null=True,blank=True)
    cover_image=models.ImageField("cover_image/",null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField()



def __str__(self):
    return self.user.username()
    

    
