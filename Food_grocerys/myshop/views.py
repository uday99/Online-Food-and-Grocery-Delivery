from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,'myshoptemplate/index.html')


def register(request):
    return render(request,'myshoptemplate/register.html')