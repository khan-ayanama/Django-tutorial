# Notes02

## URls

URls are the set patterns of which browser requests and it hits the correct View function/Class and returns the http response or simple HTML template.  
Every URL has it's view

## Views

Django views are Python functions/Class that takes http requests and returns some response like http response or HTML documents.

## How to integrate URLs and Views

1.First Create views.py file in a same folder as urls.py  
2.Import HtttpResponse in views.py from django.http  
3.Create a function in views.py with a parameter request  

```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Welcome to Home page!!")
```  

4.In urls.py import views from folderName  
5.Add the url path name and it's target view  

```python
from Tutorial02 import views

urlpatterns = [
    path('', views.home),
]
```

## Dynamic URL in Django

### URls are of 3 types:-

1. Integer type {int}  
2. String type {str}  
3. Slug type {slug}  

### Plan

Let's create a View of name course which will be the home page for courses and then we will add a different type of urls for each course  

### Courses page setup

* VIEW

    ```python
    def courses(request):
        return HttpResponse('Welcome to courses Section!!')
    ```  

* URL  

    ``` python
        path('courses/', views.courses),
    ```

### 1.Integer type URL

* View  

    ```python
    def course_detail(requst,courseid):
        return HttpResponse(f'course number is {courseid}')
    ```

* URL

    ```python
        path('courses/<int:courseid>', views.course_detail),
    ```

### 2.String type URL

View will be same as in Integer type  

* URL

    ```python
        path('courses/<int:courseid>', views.course_detail),
    ```

### 3.Slug Type URL

* URL

    ```python
        path('courses/<slug:courseid>', views.course_detail),
    ```

## Template as a Response

1. import a render from a django.shortcuts in views
2. Create a View and return a html page algong with request

    ```python
    from django.shortcuts import render

    def home(request):
        return render(request,'index.html')
    ```

3. Create the index.html file in the template folder which should be in the Base Directory
4. Add the template file location in settings in TEMPLATES inside DIRS

    ```python
    'DIRS': [BASE_DIR,'templates']
    ```

## Passing data from View to Template

1. To pass the data in view function create a dictionary of data you want to pass and pass <b>Three</b> parameters

    ```python
    def about_us(request):
        data = {
            'title':'About Section',
            'page_detail': 'About-Us section'
        }
        return render(request,'about-us.html',data)
    ```

2. In about-us page use {{ data }} -> double curly braces to recieve data

    ```html
        <title>{{title}}</title>
        <h1>Hello welcome to {{page_detail}}</h1>
    ```

## For Loop in template

1. When data passed in list format

   * View

        ```python
        def about_us(request):
            data = {
                'city_names': ['Lucknow','Benaras','Delhi'],
            }
            return render(request,'about-us.html',data)
        ```

   * Template

        ```html
        {% for city in city_names %}
        <div class="city-name">{{city}}</div>
        {% endfor %}
        ```

2. When data passed in dictionary format

    * View

        ```python
        def about_us(request):
            data = {
                'person_info': [
                {'name':'Ayan','phone':1234567890},
                {'name':'Naeem','phone':238675321},
                ]
            }
            return render(request,'about-us.html',data)
        ```

    * Template

        ```html
        <table border="1">
        <thead>
            <th>Name</th>
            <th>Phone</th>
        </thead>
        {% for person in person_info %}
        <tbody>
            <td>{{person.name}}</td>
            <td>{{person.phone}}</td>
        </tbody>
        {% endfor %}
        </table>
        ```

## If else statement in template

```html
{% for city in city_names %}
    {% if city|length > 5 %}
    <div class="city-name">{{city}}</div>
    {% else %}
        City is not available
    {% endif %}
{% endfor %}
```
