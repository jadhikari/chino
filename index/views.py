from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(request,'index/index.html')

def chino(request):
    return render(request, 'index.html')