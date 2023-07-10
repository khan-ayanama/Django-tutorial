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
