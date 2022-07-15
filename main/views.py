from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    subject = 'welcome to GFG world'
    message = 'Hi Rajwinder, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['iamkarantalwar@gmail.com' ]    
    send_mail( subject, message, email_from, recipient_list ) 
    return render(request, 'index.html')

def findcounsellor(request):
    return render(request, 'find-counsellor.html')

def counsellorinfo(request):
    return render(request, 'counsellor-info.html')

def signup(request):
    return render(request, 'sign-up.html')

def signup1(request):
    return render(request, 'sign-up1.html')

def signup2(request):
    return render(request, 'sign-up2.html')

def signup3(request):
    return render(request, 'sign-up3.html')