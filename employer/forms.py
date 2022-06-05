from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class Jobform(forms.Form):
#     job_title=forms.CharField()
#     company_name=forms.CharField()
#     location=forms.CharField()
#     salary=forms.IntegerField()
#     experiernce=forms.IntegerField()

class Jobform(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"  #for all fields
        # fields=["field1","field2"] - if we want only some fields then mention that field
        # exclude=["field"]  - if we have 10 fields and we only want 9 fields and didnt want the remaining 1 field then mention that 1 field in exclude

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password1","password2"]

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
