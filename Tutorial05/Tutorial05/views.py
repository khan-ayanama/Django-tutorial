from django.shortcuts import render
from services.models import Services
from news.models import News


def home(request):
    # service_data = Services.objects.all().order_by('-service_title')[:3]

    service_data = Services.objects.all()
    news_data = News.objects.all()

    if request.method == 'GET':
        service_searched = request.GET.get('servicename')
        if service_searched != None:
            service_data = Services.objects.filter(service_title__icontains = service_searched)

    data = {
        'service_data':service_data,
        'news_data': news_data
    }
    return render(request,'index.html',data)

def news_details(request,id):
    news_data = News.objects.get(id = id)
    data = {
        'news_data':news_data
    }
    return render(request,'news-detail.html',data)