from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about-us.html')

def contact_us(request):
    return render(request,'contact-us.html')

def services(request):
    return render(request,'our-services.html')

