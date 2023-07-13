from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .form import user_form

def home(request):
    final_ans = 0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        final_ans = n1+n2
    except:
        pass
    return render(request,'index.html',{'output':final_ans})


def post_method(request):
    final_ans = 0
    try:
        # n1 = int(request.POST['num1'])
        # n2 = int(request.POST['num2'])
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        final_ans = n1+n2

        url = f"/thanks/?output={final_ans}"

        return HttpResponseRedirect(url)
        
    except:
        pass
    return render(request,'form2.html',{'output':final_ans})

def thanks(request):
    if request.method == 'GET':
        ans = request.GET.get('output')
        print(ans)
    return render(request,'thanks.html',{'ans':ans})

def submit_form(request):
    ans = 0
    if request.method == 'GET':
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        ans = n1 + n2
    return HttpResponse(ans)

def django_form(request):
    fn = user_form()
    data = {'form':fn}
    return render(request,'django-form.html',data)