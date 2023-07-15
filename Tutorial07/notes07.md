# Notes - 07

## Save data from form

1. First define the model of the fields you want to add in database

    ```python
        from django.db import models

        # Create your models here.
        class ContactEnquiry(models.Model):
            name = models.CharField(max_length=50,blank=True,default='',null=True)
            email = models.CharField(max_length=50,blank=True,default='',null=True)
            subject = models.CharField(max_length=50,blank=True,default='',null=True)
            message = models.TextField(blank=True,default='',null=True)
    ```

2. Create a view and assign the value of the form received by templates to DataBase

    ```python
        from django.shortcuts import render
        from contact.models import ContactEnquiry

        def home(request):
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                submit = ContactEnquiry(name=name,email=email,subject=subject,message=message)
                submit.save()

            return render(request,'index.html')
    ```

## Upload a File in Django Model

1. Create a folder 'media' in parent directory

2. Open settings.py and define two things

    ```python
        MEDIA_ROOT = BASE_DIR/"media"

        MEDIA_URL = '/media/'
    ```

3. In URL import functions

    ```python
        from django.conf import settings
        from django.conf.urls.static import static
    ```

4. In urls.py add this function

    ```python
        if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    ```

5. Add image field in model and then migrate

    ```python
        image = models.FileField(upload_to='contact/',max_length=250,default=None,null=True)
    ```

## Display image uploaded on template

1. First get the fields from the model in view and render to html page

    ```python
        def home(request):
        contact_details = ContactEnquiry.objects.all()
        
        data = {
            'contact_details':contact_details
        }

        return render(request,'index.html',data)
    ```

2. Receive the image and parse it on html page

    ```html
        {% for n in contact_details %}
        <img src="/media/{{n.image}}" alt="page not rendered yet">
        <h2>{{n.email}}</h2>
        {% endfor %}
    ```

## Sending Email

1. First allow in gmail account less secure app

2. In settings.py add info

    ```python
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_PORT = 587
        EMAIL_HOST_USER = 'mailws1990@gmail.com'
        EMAIL_HOST_PASSWORD = 'Mail@123!!'
        EMAIL_USE_TLS = True
    ```

3. Import library and compose message and send in views.py

    ```python
        from django.core.mail import send_mail

        def home(request):
            send_mail(
                'Testing mail',
                'Is mail send or not',
                'mailws1990@gmail.com',
                ['impracticalayan@gmail.com'],
                fail_silently=False
            )
            
            return render(request,'index.html')
    ```

## Send html content on mail

```python
        from django.core.mail import send_mail,EmailMultiAlternatives

        def home(request):
           subject = 'Testing mail'
           form_email = 'abc@gmail.com'
           msg = '<p>Hello <b>name</b> </p>'
           to = 'xyz@gmail.com'
           msg = EmailMultiAlternatives[subject,msg,form_email,[to]]
           msg.content_subtype = 'html'
           msg.send()
            
            return render(request,'index.html')
    ```
