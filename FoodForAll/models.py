	
from email.policy import default
from django.db import models

# Create your models here.
# model for all users 
class   myUser(models.Model):
    usert=(
        ("ngo","NGO"),("doner","Doner")
    )
    usertype=models.CharField(max_length=5,default='',choices=usert)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default='')
    phoneno=models.CharField(max_length=50,default = '')
    password=models.CharField(max_length=50)
   
    def __str__(Self):
        return Self.username


class donatefoods(models.Model):
    foodforr=(
        ("animal","ANIMAL"),("human","HUMAN")
    )
    foodfor=models.CharField(max_length=7,default='',choices=foodforr)
    foodtype=models.CharField(max_length=50,default='')
    quantity=models.CharField(max_length=50,default='')
    dateofc=models.DateField(default='')
    expdate=models.DateField(default='')
    timeofc=models.TimeField(default='')
    address=models.CharField(max_length=500,default='')
    Image=models.ImageField(upload_to="media",default='')
    def __str__(Self):
        return Self.foodtype
# class Images(model.models):
#     name= models.CharField(max_length=500)
#     videofile= models.FileField(upload_to='/static/Image', null=True, verbose_name="")

    # def __str__(self):
    #     return self.name + ": " + str(self.imagefile)