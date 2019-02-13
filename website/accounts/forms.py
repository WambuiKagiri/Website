from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth import (
authenticate,
get_user_model,
logout,
)

User = get_user_model()

class loginform(forms.Form):
    username = forms.CharField(label="username",max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':'username'}))
    password = forms.CharField(label="password",max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password'}))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password=password)

        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 1:
            user = user_qs.first()
            if not user.is_active:
                raise forms.ValidationError("This user is not active")


        if not user:
            raise forms.ValidationError("This user does not exist")

        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password!")

        if user.groups.filter(name='Agents').exists() == False and user.groups.filter(name='Clients').exists():
            raise forms.ValidationError("Sorry, you are not permitted to access this page")

        return super(loginform,self).clean(*args,**kwargs)
