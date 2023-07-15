# Notes - 05

## Django Models

Django uses to create tables, their fields, and various constraints. In short, Django Models is the SQL of Database one uses with Django.

## Create Models in Django

1. Create an APP

    ```python
    python manage.py startapp <App Name>
    ```

2. In the models.py of app section create a fields which you want to change dynamically

    ```python
        from django.db import models

        class Services(models.Model):
            service_icon = models.CharField(max_length=50)
            service_title = models.CharField(max_length=50)
            service_description = models.TextField()
    ```

3. Add App name in the settings.py of main folder in InstalledApps

    ```python
        INSTALLED_APPS = [
            'django.contrib.staticfiles',

            'services',
        ]
    ```

4. To create model in database you have to run 2 commands

    ```python
        python manage.py makemigrations

        python manage.py migrate
    ```

5. To Access admin panel you need to create Super User

    ```python
        python manage.py createsuperuser
    ```

6. In admin.py of app section register the model so that it appear in the admin panel

    ```python
        from django.contrib import admin
        from services.models import Services

        class ServiceAdmin(admin.ModelAdmin):
            list_display = ('service_icon','service_title','service_description')

        # Register your models here.
        admin.site.register(Services,ServiceAdmin)
    ```

## Fetch Data from Models

1. In View section import model from app and then fetch data in view function and pass it to HTML page

    ```python
        from django.shortcuts import render

        # Importing models from Services App
        from services.models import Services

        def home(request):
            service_data = Services.objects.all()
            data = {
                'service_data':service_data
            }
            return render(request,'index.html',data)
    ```

2. Parse data in HTML Page

    ```html
        <div class="container">

            {% for model_data in service_data %}

            <div class="card-content">
                <div class="card-header">

                    <div class="card-icon">{{model_data.service_icon}}</div>
                    <div class="card-title">{{model_data.service_title}}</div>
                </div>
                <div class="card-description">{{model_data.service_description}}</div>

            </div>
                {% endfor %}

        </div>
    ```

### Fetching data from models in Ascending or Descending order using orderby

1. Here data will fetch in Ascending order

    ```python

        def home(request):
            service_data = Services.objects.all().order_by('service_title')
            data = {
                'service_data':service_data
            }
            return render(request,'index.html',data)
    ```

2. Data in Descending order

    ```python

        def home(request):

            # Minus sign before service title will render data in descending order

            service_data = Services.objects.all().order_by('-service_title')
            data = {
                'service_data':service_data
            }
            return render(request,'index.html',data)
    ```

## Limiting Query Result

Numbers of result you wan't to show

```python

    def home(request):
        service_data = Services.objects.all().order_by('service_title')[:3]
        data = {
            'service_data':service_data
        }
        return render(request,'index.html',data)
```

## Template Filters

This is used for string formatting

```django
    <div class="card-description">{{model_data.service_description | upper}}</div>
```

## Django TinyMce Integration in the new app called NEWS

1. Installation

    ```python
        pip install django-tinymce
    ```

2. Add tinymce in Installed apps of settings.py

3. While creating models import tinymce and use it while defining fields

    ```python
    from django.db import models
    from tinymce.models import HTMLField

    # Create your models here.

    class News(models.Model):
        news_title = models.CharField(max_length=100)
        news_description = HTMLField()
    ```

4. After that run command for makemigrations and migrate

## News app

### Marquee tag on index.html

1. First import news in views from models

    ```python
        from django.shortcuts import render
        from news.models import News

        def home(request):
            news_data = News.objects.all()
            data = {
                'news_data': news_data
            }
            return render(request,'index.html',data)
    ```

2. Render data in marquee tag of html page

    ```html
        <marquee>
            {% for head in news_data %}

            <a href=""> {{head.news_title}} </a> &nbsp;&nbsp;| &nbsp;&nbsp;

            {% endfor %}

        </marquee>

    ```

3. Create a url for news detail page where you want to go when you click on marquee tag

    ```python
        path('news-detail/<id>',views.news_details)
    ```

4. Add a link in marquee tag when clicking

    ```html
        <a href="/news-detail/{{head.id}}"> {{head.news_title}} </a> &nbsp;&nbsp;| &nbsp;&nbsp;
    ```

5. Create a view which will take an id and render the news-detail page

    ```python
        def news_details(request,id):
            news_data = News.objects.get(id = id)
            data = {
                'news_data':news_data
            }
            return render(request,'news-detail.html',data)
    ```

6. Recieve data on news-detail page and render the data

    ```html
        <div class="container">
            <h2>{{news_data.news_title}}</h2>
            <p>{{news_data.news_description | safe}}</p>
        </div>
    ```

## Reset Django Admin password without forget

```python
    python manage.py changepassword <user_name>
```

## Django Filter

1. Make a Search Bar at template page

    ```html
    <form style="text-align: center;" method="get">
        <input type="text" name="servicename">
        <input type="submit" value="Search">
    </form>
    ```

2. In View function filter the result fetched from models

   - It will search the exact word

        ```python
            from django.shortcuts import render
            from services.models import Services


            def home(request):
                service_data = Services.objects.all()

                if request.method == 'GET':
                    service_searched = request.GET.get('servicename')
                    if service_searched != None:
                        service_data = Services.objects.filter(service_title = service_searched)

                data = {
                    'service_data':service_data,
                }
                return render(request,'index.html',data)
        ```

   - If you want to search from the single word

        ```python
            from django.shortcuts import render
            from services.models import Services


            def home(request):
                service_data = Services.objects.all()

                if request.method == 'GET':
                    service_searched = request.GET.get('servicename')
                    if service_searched != None:
                        service_data = Services.objects.filter(service_title__icontains = service_searched)

                data = {
                    'service_data':service_data,
                }
                return render(request,'index.html',data)
        ```

3. When No data found use empty tag in html

    ```html
        {% for model_data in service_data %}

                <div class="card-content">
                    <div class="card-header">
                        <div class="card-icon">{{model_data.service_icon}}</div>
                        <div class="card-title">{{model_data.service_title}}</div>
                    </div>
                    <!-- <div class="card-description">{{model_data.service_description | upper}}</div> -->

                    <div class="card-description">{{model_data.service_description | safe}}</div>
                </div>
                {% empty %}
                No data found
                {% endfor %}
    ```

## Django Auto-Slug

1. First of all we need to install auto-slug

    ```python
        pip install django-autoslug
    ```

2. In models.py of news section import Autoslug and add the function in the class of model

    ```python
        from django.db import models
        from tinymce.models import HTMLField

        from autoslug import AutoSlugField

        # Create your models here.

        class News(models.Model):
            news_title = models.CharField(max_length=100)
            news_description = HTMLField()

            news_slug = AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)
    ```

3. Now migrate all the new field created in model using makemigrations command

4. Change the link tag and call the news_slug field from the database

    ```html
        <a href="/news-detail/{{head.news_slug}}"> {{head.news_title}} </a> &nbsp;&nbsp;| &nbsp;&nbsp;
    ```

5. Change the url to slug

    ```python
        path('news-detail/<slug>',views.news_details)
    ```

6. Receive the slug in view of news and change the recieved field in get function

    ```python
        def news_details(request,slug):
        news_data = News.objects.get(slug_field = slug)
        data = {
            'news_data':news_data
        }
        return render(request,'news-detail.html',data)
    ```