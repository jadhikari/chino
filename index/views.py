from django.shortcuts import render 
from django.http.response import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



def chino(request):
    return render(request, 'main.html')

def about(request):
    return render(request,'about.html')

# def calendar(request):
#     return render(request, 'calendar.html')

def company(request):
    return render(request,'company.html')

def contact(request):
    # if request.method == "POST":
    #     title = request.POST['title']
    #     name = request.POST['name']
    #     phone = request.POST['phone']
    #     email = request.POST['email']
    #     text = request.POST['text'] 
    #     #send a email
    #     send_mail(
    #         title,
    #         'Name of sender : ' + name,
    #         'Phone number of sender : ' + phone,
    #         ' Messages : ' + text,
    #         email,
    #         ['info@mychino.jp'],
    #         fail_silently=False,

    #     )
    #     return render(request,'contact.html')
    # else:
       return render(request,'contact.html')  

def components(request):
    return render(request,'components.html')