from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User 
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلا ثبت شده است.")
        
        return email
    


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است.")
        
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
            "class": "form-input",
            "placeholder": "نام کاربری",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
            "class": "form-input",
            "placeholder": "ایمیل",
            }
        )
        self.fields["phone_number"].widget.attrs.update(
            {
            "class": "form-input",
            "placeholder": "شماره تلفن",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
            "class": "form-input",
            "placeholder": "رمز عبور",  
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
            "class": "form-input",
            "placeholder": "تکرار رمز عبور",  
            }
        )



class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({

            "class": "form-input",
            "placeholder": "نام کاربری",

        })

        self.fields["password"].widget.attrs.update({

            "class": "form-input",
            "placeholder": "رمز عبور",

        })