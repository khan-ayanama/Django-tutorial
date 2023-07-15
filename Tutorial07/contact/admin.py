from django.contrib import admin
from .models import ContactEnquiry

# Register your models here.
class ContactForm(admin.ModelAdmin):
    list_display = ['name','email','subject','message','image']


admin.site.register(ContactEnquiry,ContactForm)