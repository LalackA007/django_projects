from django.db import models
<<<<<<< HEAD
from django.conf import settings

class Profile(models.Model):
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Profile of {self.user.username}'
=======

# Create your models here.
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
