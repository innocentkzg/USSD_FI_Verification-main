from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Institution

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'phonenumber')
class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['tin', 'name', 'category', 'status', 'description', 'phone_number']

