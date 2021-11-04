from django.shortcuts import render 
from django.http.response import HttpResponse, JsonResponse
# Create your views here.



def chino(request):
    return render(request, 'main.html')

def about(request):
    return render(request,'about.html')
