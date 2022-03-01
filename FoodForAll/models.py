	
from datetime import datetime
from email.mime import message
from email.policy import default
from operator import mod
from pyexpat import model
from time import time
from django.db import models

# Create your models here.
# model for all users 
class   myUser(models.Model):
    usert=(
        ("ngo","NGO"),("doner","Doner"),("consumer","consumer")
    )
    usertype=models.CharField(max_length=10,default='',choices=usert)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=50)
    
    def __str__(Self):
        return Self.username


class donation(models.Model):
    foodt=(
        ("rice","rice"),("wheat","wheat"),("corn","corn")
    )
    foodtype=models.CharField(max_length=50,default='',choices=foodt)
    quantity=models.IntegerField(default=0)
    dateofc=models.DateField(default='')
    timeofc=models.TimeField(default='')
    image = models.ImageField(upload_to="myimage",default='')
    address=models.CharField(max_length=500,default='')
    status=models.CharField(max_length=10,default='Pending')  
    user=models.ForeignKey(myUser,on_delete=models.CASCADE)
    def __str__(Self):
        return Self.foodtype


class userdetail(models.Model):
    g=(
        ("male","MALE"),("female","FEMALE")
    )
    gender=models.CharField(max_length=7,default='',choices=g)
    firstname=models.CharField(max_length=50,default='')
    lastname=models.CharField(max_length=50,default='')
    bdate=models.DateField(default='')
    phoneno=models.CharField(max_length=50,default = '')
    aadhar=models.CharField(max_length=50,default = '')
    address=models.CharField(max_length=500,default='')
    user=models.ForeignKey(myUser,on_delete=models.CASCADE)
    def __str__(Self):
        return Self.firstname

class fooddata(models.Model):
    foodtype=models.CharField(max_length=50,default='')
    quantity=models.IntegerField(default=0)
    available=models.BooleanField(default=False)
    message=models.BooleanField(default=False)
    # image = models.ImageField(upload_to='images',default='')
    def __str__(Self):
        return Self.foodtype
# cart model

class cart(models.Model):
    user=models.ForeignKey(myUser,on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=datetime.now)
    def __str__(Self):
        return Self.user.username

class cartItem(models.Model):
    foodtype=models.ForeignKey(fooddata,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=10,default=0)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    def __str__(Self):
        return Self.foodtype.foodtype

class feedback(models.Model):
    desc=models.CharField(max_length=500)
    pic=models.ImageField(upload_to="con_pic",null=True)
    def __str__(self):
        return self.desc

