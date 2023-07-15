from django.db import models

# Create your models here.
class ContactEnquiry(models.Model):
    name = models.CharField(max_length=50,blank=True,default=None,null=True)
    email = models.CharField(max_length=50,blank=True,default='',null=True)
    subject = models.CharField(max_length=50,blank=True,default='',null=True)
    message = models.TextField(blank=True,default='',null=True)
    image = models.FileField(upload_to='contact/',max_length=250,default=None,null=True)