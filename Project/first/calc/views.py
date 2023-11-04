from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'veleswaran'})

def add(request):
    val=int(request.GET['num'])
    val1=int(request.GET['num1'])
    res=val+val1
    return render(request,'result.html',{'result':res})