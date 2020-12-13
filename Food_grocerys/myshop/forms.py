from django import  forms
from myshop.models import RegistrationModel
import random
from django.core.mail import send_mail
from Food_grocerys.settings import EMAIL_HOST_USER
from myshop.utils import sendTextMessage

class RegisterForm(forms.ModelForm):

    def clean_otp(self):
        email=self.cleaned_data['email']
        cno=self.cleaned_data['contact']

        #generating random numbers
        otp = random.randint(100000,999999)

        #sending otpp to email as message
        subject="your otp "
        message= str(otp)+'is your otp for online Foodmart and Grocery '
        send_mail(subject,message,EMAIL_HOST_USER,[email])

        #sending Otp as textmsg to contactno

        sendTextMessage(message,cno)

        return otp






    class Meta:
        model=RegistrationModel
        exclude =('status',)
        labels={'name':'Name','contact':'Contactno','email':'Email'}
        widgets={
            'password' : forms.PasswordInput
        }


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=150,label='Email')
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
