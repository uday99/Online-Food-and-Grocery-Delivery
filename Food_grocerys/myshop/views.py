from django.shortcuts import render,redirect
from myshop.models import RegistrationModel
from myshop.forms import RegisterForm

# Create your views here.
def showIndex(request):
    return render(request,'myshoptemplate/index.html')


def register(request):
    rf=RegisterForm(request.POST)

    if request.method == "POST":
        if rf.is_valid():
            rf.save()
            return redirect('user-otp')
        else:
            return render(request, 'myshoptemplate/register.html', {'rf': rf})

    else:
        return render(request,'myshoptemplate/register.html',{'rf':rf})


def userOtp(request):


    return render(request, "myshoptemplate/user-otp.html")