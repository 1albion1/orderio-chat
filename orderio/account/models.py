from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.username
    
    def get_profile_pic_url(self):
        pic_url = self.employee.profile_pic.url
        if pic_url:
            return pic_url
        else:
            return '/img/default.png'