# Notes - 04

## Implement form with GET method

1. First of all set the method of the from is GET
2. Set the name of input in form

    ```html
        <input type="text" name="num2">
    ```

3. Recieve input in view from request and add them and return along with index.html file

    ```python
    def home(request):
        final_ans = 0
        try:
            n1 = int(request.GET['num1'])
            n2 = int(request.GET['num2'])
            final_ans = n1+n2
        except:
            pass
        return render(request,'index.html',{'output':final_ans})
    ```

4. Second Method

    ```python
    def home(request):
        final_ans = 0
        try:
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            final_ans = n1+n2
        except:
            pass
        return render(request,'index.html',{'output':final_ans})
    ```

## POST method with CSRF Token

1. Add csrf token in html form

    ```python
        {% csrf_token %}
    ```

2. Evaluate the value and return the ans

    ```python
    def home(request):
        final_ans = 0
        try:
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            final_ans = n1+n2
        except:
            pass
        return render(request,'index.html',{'output':final_ans})
    ```

## Page Redirection

Page Redirection is a method when you submit or complete task the page automatically changes to thank you or some thing else

1. First of all import HttpResponseRedirect from django.http

    ```python
        from django.http import HttpResponseRedirect
    ```

    - You can also use redirect method instead of HttpResponseRedirect.

        ```python
            from django.shortcut import redirect
        ```

2. Return the HttpResponseRedirect argument the link you want to get redirected

    ```python
    def post_method(request):
        final_ans = 0
        try:
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            final_ans = n1+n2

            return HttpResponseRedirect('/thanks')

        except:
            pass
        return render(request,'form2.html',{'output':final_ans})
    ```

### Page Redirection with some value with it

1. Send the value in the url

    ```python
        def post_method(request):
            final_ans = 0
            try:
                n1 = int(request.POST['num1'])
                n2 = int(request.POST['num2'])
                final_ans = n1+n2

                url = '/thanks/?output={}'.format(final_ans)

                return HttpResponseRedirect(url)

            except:
                pass
            return render(request,'form2.html',{'output':final_ans})
    ```

2. Recieve the value by the view function of the redirected page and pass it to page

    ```python
    def thanks(request):
        if request.method == 'GET':
            ans = request.GET.get('output')
            print(ans)
        return render(request,'thanks.html',{'ans':ans})
    ```

3. Receive the value at the page and print it.

    ```html
        <h2>Answer is : {{ans}}</h2>
    ```

## HTML Form Action URL

Action method also used to redirect page

1. First create specifiy the url you want to redirect in Action attribute of form

    ```html
        <form method="GET" action="{% url 'submit-form' %}">
    ```

2. Pass the values in submit_form view and print it.

    ```python
        def submit_form(request):
        ans = 0
        if request.method == 'GET':
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            ans = n1 + n2
        return HttpResponse(ans)
    ```

## Django Forms

1. Create python file forms.py and create a django form inside it

    ```python
    from django import forms

    class user_form(forms.Form):
        num1 = forms.CharField(label='Value1')
        num2 = forms.CharField(label='Value2')
        email = forms.EmailField()
    ```

2. Create a url where you want to render this django form

    ```python
        path('django-form/',views.django_form,name="django-form")
    ```

3. Create a view and render the html page where you want to render the form

    ```python
        def django_form(request):
        fn = user_form()
        data = {'form':fn}
        return render(request,'django-form.html',data)
    ```
