from django.shortcuts import render,redirect
from myshop.models import RegistrationModel,ProfileModel
from myshop.forms import RegisterForm,LoginForm,ProfileForm
from django.contrib import messages

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


def validateOTp(request):
    em=request.POST.get('t1')
    cn=request.POST.get('t2')
    otp=request.POST.get('t3')
    try:
        result=RegistrationModel.objects.get(email=em,contact=cn,otp=otp)
        if result.status == "pending":
            result.status = "approved"
            result.save()
            messages.success(request,"Thanks for Registration")
            return redirect('confirmation')
        elif result.status == "approved":
            messages.success(request,"Your Registration is Already Approved")
            return redirect('confirmation')

    except RegistrationModel.DoesNotExist:
        message="sorry invalid details pls try again"
        return  render(request,'myshoptemplate/user-otp.html',{'error': message})


def confirmation(request):
    return render(request,'myshoptemplate/confirmation.html')


def loginPage(request):
    lf = LoginForm(request.POST)
    if request.method == 'POST':
        if lf.is_valid():
            try:
                em=request.POST.get('email')
                pwd=request.POST.get('password')
                result=RegistrationModel.objects.get(email=em,password=pwd)
                if result.status == "pending":
                    error="Sorry Your Registration is Pending..."
                    return render(request,"myshoptemplate/login.html",{'error':error})
                if result.status == "closed":
                    error="Sorry your account is closed Cannotlogin"
                    return render(request,"myshoptemplate/login.html",{'error':error})
                request.session["contact"]= result.contact
                request.session["name"]= result.name
                request.session["rno"]= result.rno
                return  redirect('v_profile')

            except RegistrationModel.DoesNotExist:
                return render(request,'myshoptemplate/login.html',{'lf':lf,'error':'Invalid Username/password'})

        else:
            return render(request, 'myshoptemplate/login.html', {'lf': lf})

    else:
        return render(request,'myshoptemplate/login.html',{'lf':lf})


def welcomePage(request):


    return render(request,"welcome.html")


def viewProfile(request):
    try:
        if request.session["name"]:
            try:
                result=ProfileModel.objects.get(person__name=request.session['name'])
                status=True
                return render(request, 'myshoptemplate/v_profile.html', {"status": status, 'result': result})
            except ProfileModel.DoesNotExist:
                status=False
                return render(request, 'myshoptemplate/v_profile.html', {"status": status})
        else:
            return  render(request,'myshoptemplate/v_profile.html')
    except KeyError:
        return render(request, 'myshoptemplate/v_profile.html')






def logoutProfile(request):
    try:
        del request.session["contact"]
        del request.session["name"]
        del request.session["rno"]
        return redirect('main')
    except KeyError:

        return render(request,"myshoptemplate/login.html",{"error":"Please do Login",'lf':LoginForm()})


def updatePro(request):
    try:
        if request.session['name']:
            try:
                p=request.POST.get('p1')
                g=request.POST.get('p2')
                db=request.POST.get('p3')
                add=request.POST.get('p4')
                img=request.FILES['p5']
                name=request.session['name']
                print(name)
                pm=ProfileModel.objects.get(person__name=name)
                print("welocme")
#       rm=RegistrationModel.objects.get(name=name)
                pm.gender=g
                pm.dob=db
                pm.address=add
                pm.image=img
                pm.save()
                return redirect('v_profile')
            except ProfileModel.DoesNotExist:
                print('bye')
                return render(request, "myshoptemplate/updateprof.html")
        else:
            return render(request, "myshoptemplate/updateprof.html")
    except KeyError:
        return render(request, "myshoptemplate/updateprof.html")


def deleteProfile(request):
    try:
        if request.session['name']:
            try:
                name=request.session['name']
                status = False
                return render(request, 'myshoptemplate/v_profile.html', {"status": status})
            except ProfileModel.DoesNotExist:
                return render(request,'myshoptemplate/v_profile.html')
        else:
            return render(request, 'myshoptemplate/v_profile.html')


    except KeyError:
        return render(request,'myshoptemplate/v_profile.html')