<<<<<<< HEAD
from .models import Profile
from django import forms
from django.contrib.auth import get_user_model

=======
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = get_user_model()
<<<<<<< HEAD
        fields = ['username', 'first_name', 'email']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate', 'photo']
=======
        fields = ['username', 'first_name', 'email']
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
