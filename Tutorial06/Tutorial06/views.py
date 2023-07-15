from django.shortcuts import render
from services.models import Services
from django.core.paginator import Paginator

def home(request):
    service_data = Services.objects.all()

    display_pages = Paginator(service_data,2)
    default_page = request.GET.get('page')
    current_page = display_pages.get_page(default_page)
    total_page = current_page.paginator.num_pages

    data = {
        'service_data':current_page,
        'total_pages': [n+1 for n in range(total_page)]
    }
    return render(request,'index.html',data)