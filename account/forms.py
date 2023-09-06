from django import forms
from account.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(required=False)
    mobile_phone = forms.CharField(max_length=20, required=False)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    favourite_national_team = forms.CharField(max_length=100, required=False)
    favourite_city = forms.CharField(max_length=100, required=False)
    favourite_language = forms.CharField(max_length=100, required=False)
    club_de_coeur = forms.CharField(max_length=100, required=False)




class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'password': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }