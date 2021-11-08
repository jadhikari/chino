from django.shortcuts import render 
from django.http.response import HttpResponse, JsonResponse
# Create your views here.



def chino(request):
    return render(request, 'main.html')

def about(request):
    return render(request,'about.html')

def calendar(request):
    return render(request, 'calendar.html')

def company(request):
    return render(request,'company.html')

def contact(request):
    return render(request,'contact.html')

def components(request):
    return render(request,'components.html')