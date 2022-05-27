from django import forms
from app.models import FaceRecognition
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class FaceRecognitionform(forms.ModelForm):

    class Meta:
        model = FaceRecognition
        fields =['image']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']