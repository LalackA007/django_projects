from django.contrib import admin
<<<<<<< HEAD
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthdate', 'photo']
=======

# Register your models here.
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
