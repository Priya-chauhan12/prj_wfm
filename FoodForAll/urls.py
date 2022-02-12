
from django.contrib import admin 
from django.urls import path
from FoodForAll import views

urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('homeuser',views.homeuser,name='homeuser'),
    path('homengo',views.homengo,name='homengo'),
    
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('registerview',views.registerview,name='registerview'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),

    path('userBase',views.userBase,name='userHome'),
    path('users',views.users,name='users'),
    path('userdetail',views.userdetail,name='userdetail'),
    path('donatefood',views.donatefood,name='donatefood'),
    
    path('ngo',views.ngoBase,name='ngo'),
    path('ngodetail',views.ngodetail,name='ngodetail'),
    path('ngopage',views.ngopage,name='ngopage'),
    path('viewdonationrequest',views.viewdonationrequest,name='viewdonationrequest'),

    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('aboutuser',views.aboutuser,name='aboutuser'),
    path('contactuser',views.contactuser,name='contactuser'),
    path('aboutngo',views.aboutngo,name='aboutngo'),
    path('contactngo',views.contactngo,name='contactngo'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('managegallary',views.managegallary,name='managegallary'),
    

    
]
