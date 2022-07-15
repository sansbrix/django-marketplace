from django.shortcuts import render

# Create your views here.
def index(request):
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