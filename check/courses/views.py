from django.shortcuts import render

# Create your views here.

def mysql(request):
    return render(request,"mysql.html")