from django.db import models
from django.contrib.auth.models import User       #   importing the existing modles
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # for image field first you have to install a new package called pillow
    image = models.ImageField(upload_to='profile_pictures',default='profilepic.jpg')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username