# Notes Day1

## WHAT IS FRAMEWORK?

A framework is a particular set of rules, ideas or beliefs

## WHAT IS DJANGO?

1.It is high level web application framework  
2.Follows model-view-template  
3.It's fast, secure and well established  
4.Built in Authentication and Authorization  
5.Packaging System  
6.Youtube, Insta, Spotify, Dropbox

## WHAT IS MVT?

1.Model View Template  
2.Model --> Model is going to act as the interface of your data.  
3.View --> The View is user Interface, which you want to render a website  
4.Template --> HTML Files  

## FLOW CHART OF MVT

User --> Django --> URL --> View --> Model & Template

## INSTALLING PYTHON AND DJANGO

1.To check python on cmd --> python  
2.pip freeze --> All installed libraries and packages  
3.To install Django --> pip install django  

## CREATING A DJANGO PROJECT

1.To create project --> django-admin startproject <project_name>

## RUN DEVELOPMENT SERVER

1.command --> python manage.py runserver  
2.CustomizedPort --> python manage.py runserver1234  

## PYTHON DJANGO STRUCTURE

1.sqlite --> Default database  
2.manage.py --> manages whole project and run  
3.templates --> All the HTML files  
4.static --> All css, javascript files  
5.media --> All Dynamic files and images  
6.settings.py --> It has all project settings  
7.URLs --> All the urls of webpage connected to views.py  
8.Views.py --> All the function of the URLS  

## MIGRATE DEFAULT MIGRATIONS

1.To create the schema of database --> python manage.py makemigrations    
2.To create table --> python manage.py migrate  
  
## TO READ SQLITE FILE

We need to install db browser for sqlite

## HOW TO CREATE SUPER USER?

1.python manage.py createsuperuser  
** without migrate command you can't create superuser  

## ENDS DAY-1 AT 01:30 HRS

To be continued in Day2....
