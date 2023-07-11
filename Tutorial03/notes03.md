# Notes03

## Using CSS and JS in Project

Place all the HTML files in static folder and all CSS and JS file in static folder  

## Integrating CSS files in Project

### Method-1

1. Add location of static folder in settings.py  

    ```python
    STATICFILES_DIRS = [
        BASE_DIR,"static"
    ]
    ```

2. Changing path of CSS and JS file in html files  

   - Before

        ```html
            <link rel="stylesheet" href="assets/css/fontawesome.css">
        ```

   - After

        ```html
            <link rel="stylesheet" href="../static/assets/css/fontawesome.css">
        ```

### Method-2

1. Using Load static at the top of the html page than you only need to provide an URL inside of static folder not necessary to include static path in the URL

    ```html
    {% load static %}
    <img src="{% static 'my_app/example.jpg' %}" alt="My image">
    ```

## Include tag

It is used when there is common element across the pages of website we use include tag.

1. Steps to use include tag
   - Extract the common part and put in separate html file
   - Add the include tag at the place where you want to add the file.

        ```Python
        {% include 'header.html' %}
        ```

## Extend Tag

### Steps to Use extend keyword in Django

1. Create base.html file and include the header and footer content and between that use block to add content

    ```Python
        {% include 'header.html' %}

            {% block content %}

            {% endblock %}

        {% include 'footer.html' %}
    ```

   - Here the content will be passed between block in base.html file exactly opposite to include keyword as we have studied before

2. Add Extend keyword at the file which file you want to pass in block content

    ```python
        {% extends 'base.html' %}

        {% block content %}
            <html code>
        {% endblock %}
    ```

## URL template tag in Django - link pages

### Method - 1

- Add the link as a url defined in urls.py

    ```html
    <li><a href="/about-us">About</a></li>
    ```

- Here URL is about-us which is exactly same as defined in url

### Method - 2

1. Use name tag in urls.py

    ```python
        path('contact-us/', views.contact_us,name="contact"),
        path('services/', views.services,name="services"),
    ```

2. Then add a name with url tag in the link tag in template file.

    ```html
        <li><a href="{% url 'contact' %}">Contact</a></li>
    ```

## Highelight link in Django

1. Method - 01

   - Use if statement with request.path.  
   - request.path will give the present path

    ```html
        <li><a class="{% if request.path == '/' %} active {% endif %}" href="/">Home</a></li>
    ```

2. Method - 02

- Use Path as Alias

    ```html
        {% url 'services' as con %}

        <li><a class="{% if request.path == con %} active {% endif %}" href="{% url 'services' %}">Our Services</a>
    ```

## HTTP Methods

### GET Method

- The GET Method sends the encode user info appended to page requst.
- Sends data in url don't use if you are dealing with sensitive information.
- Only text can be transformed

### POST Method

- It transfers info via HTTP headers
- Does not have restriction of data size
- Can be used to send ASCII as well as binary data
- It is secure method
