from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def courses(request):
    return HttpResponse('Welcome to courses Section!!')

def course_detail(requst,courseid):
    return HttpResponse(f'course number is {courseid}')

def about_us(request):
    data = {
        'title':'About Section',
        'page_detail': 'About-Us section',
        'city_names': ['Lucknow','Benaras','Delhi'],
        'person_info': [
            {'name':'Ayan','phone':1234567890},
            {'name':'Naeem','phone':238675321},
        ]
    }
    return render(request,'about-us.html',data)