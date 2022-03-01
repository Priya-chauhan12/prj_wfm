
from unicodedata import name
from django.contrib import admin 
from django.urls import path
from FoodForAll import views

urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('homeuser',views.homeuser,name='homeuser'),
    path('homengo',views.homengo,name='homengo'),
     path('chome',views.chome,name='chome'),
    
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('registerview',views.registerview,name='registerview'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),

    path('userBase',views.userBase,name='userHome'),
    path('users',views.users,name='users'),
    path('userdetail',views.userdetails,name='userdetail'),
    path('donatefood',views.donatefood,name='donatefood'),
    path('donate',views.donate,name='donate'),
    path('requeststatus',views.requeststatus,name='requeststatus'),
    path('predonation',views.predonation,name='predonation'),
    
    path('ngo',views.ngoBase,name='ngo'),
    path('ngodetail',views.ngodetail,name='ngodetail'),
    path('ngopage',views.ngopage,name='ngopage'),
    path('viewdonationrequest',views.viewdonationrequest,name='viewdonationrequest'),
    path('afood',views.afood,name='afood'),
    path('confirm',views.confirm,name='confirm'),
    path('cancel',views.cancel,name='cancel'),
    path('listdoner',views.listdoner,name='listdoner'),

    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('aboutuser',views.aboutuser,name='aboutuser'),
    path('cabout',views.cabout,name='cabout'),
    path('ccontact',views.ccontact,name='ccontact'),
    path('contactuser',views.contactuser,name='contactuser'),
    path('aboutngo',views.aboutngo,name='aboutngo'),
    path('contactngo',views.contactngo,name='contactngo'),
    path('changepassword',views.changepassword,name='changepassword'),
   

    path('registration',views.registration,name='registration') ,
    path('ngoregister',views.ngoregister,name='ngoregister'),
    path('donerregister',views.donerregister,name='donerregister'),
    path('consumerregister',views.consumerregister,name='consumerregister'),
    

    path('consumer',views.consumer,name='consumer'),
    path('selectfood',views.selectfood,name='selectfood') ,
    path('select',views.select,name='select'),
    path('mycart',views.mycart,name='mycart'),
    path('order',views.order,name='order'),
    path('remove',views.remove,name='remove'),
    path('removeall',views.removeall,name='removeall'),
    path('confirmOrder',views.confirmOrder,name='confirmOrder'),
]
