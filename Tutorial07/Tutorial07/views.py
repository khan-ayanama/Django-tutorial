from django.shortcuts import render
from contact.models import ContactEnquiry
from django.core.mail import send_mail

def home(request):
    send_mail(
        'Testing mail',
        'Is mail send or not',
        'mailws1990@gmail.com',
        ['impracticalayan@gmail.com'],
        fail_silently=False
    )
    contact_details = ContactEnquiry.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        submit = ContactEnquiry(name=name,email=email,subject=subject,message=message)
        submit.save()
    data = {
        'contact_details':contact_details
    }

    return render(request,'index.html',data)