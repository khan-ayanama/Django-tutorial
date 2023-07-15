# Notes - 06

## Pagination in Django

1. Import Paginator in Views.py

    ```python
        from django.core.paginator import Paginator
    ```

2. Define the view where it will get the details of number of pages, current page or defualt page

    ```python
        def home(request):
            service_data = Services.objects.all()

            display_pages = Paginator(service_data,2)
            default_page = request.GET.get('page')
            current_page = display_pages.get_page(default_page)

            data = {
                'service_data':current_page,
            }
            return render(request,'index.html',data)
    ```

3. In template file use the pagination from bootstrap and get the pages you want to get

   - It is used for the previous and next button

    ```html
        <nav style="margin-left: 10rem;" aria-label="Page navigation example">
            <ul class="pagination">
                {% if service_data.has_previous %}
                <li class="page-item"><a class="page-link" href="/?page={{service_data.previous_page_number}}">Previous</a>
                    {% endif %}
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>

                <!-- <li class="page-item"><a class="page-link" href="#">Next</a></li> -->
                {% if service_data.has_next %}
                <li class="page-item"><a class="page-link" href="/?page={{service_data.next_page_number}}">Next</a>
                    {% endif %}
            </ul>
    ```

   - To work numbers button also add the total number of pages in views then parse it into HTML

   ```python
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

        HTML CODE 

        {% for n in total_pages %}
            <li class="page-item"><a class="page-link" href="/?page={{n}}">{{n}}</a></li>
            {% endfor %}
   ```
