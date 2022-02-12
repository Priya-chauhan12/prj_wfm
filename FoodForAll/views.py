from email import message
from email.policy import default
from urllib import request
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.template import context
from FoodForAll.models import myUser
from FoodForAll.models import donatefoods
from FoodForAll.models import Images


# ------------------------------------------------------------------------------
# for login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        # User = get_user_model()
        users = myUser.objects.all()
        for i in users:
            if i.username==username and i.password==password:
                request.session['name']=username
                usertype=i.usertype
                if usertype=='ngo':
                  return redirect('ngopage')  
                else:
                    return redirect('users')
        messages.info(request, 'Inavlid Username/Password')
        return render(request,'login.html')
    else:
        return render(request,'login.html')

# ----------------------------------------------------------------------------------------
# for registration 
def registerview(request):
    return render(request,'register.html')
def register(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        phoneno=request.POST.get('phoneno','')
        usertype=request.POST.get('usertype','')
        if password1==password2:
            user=User(password=password1,username=username,email=email)
            user.save()
            alluser=myUser(username=username,email=email,password=password1,usertype=usertype,phoneno=phoneno)
            alluser.save()
            request.session['name']=username
            messages.info(request,'Register successfully..!')
            if usertype=="ngo":
                return redirect('ngodetail')
            else:
                return redirect('userdetail')
            # return redirect('login')
        else:
            messages.info(request,'dont match password')
            return redirect('registerview')
            
    else:
        return render(request,'register.html')
# ------------------------------------------------------------------------------
# for logout
def logout(request):
    if 'name' in request.session['name']:
        print('name')
        del request.session['name']

    return redirect('login')
# --------------------------------------------------------------------------------
def donatefood(request):
    # name=request.session.get('name',default='Guest')
    if request.method=="POST":
        foodfor=request.POST['foodfor']
        foodtype=request.POST.get('foodtype','')
        quantity=request.POST.get('quantity','')
        dateofc=request.POST.get('dateofc','')
        timeofc=request.POST.get('timeofc','')
        expdate=request.POST.get('expdate','')
        address=request.POST.get('address','')
        Image=request.POST.get('Image','')
        d=donatefoods(foodfor=foodfor,foodtype=foodtype,quantity=quantity,dateofc=dateofc,timeofc=timeofc,expdate=expdate,address=address,Image=Image)
        d.save()
        return redirect('users')
    else:
        return render(request,'donatefood.html')

# ---------------------------------------------------------------------------------
def viewdonationrequest(request):
    name=request.session.get('name',default='Guest')
    # for d in donatefoods.objects.all():
    d=list(donatefoods.objects.all() ) 
    # print(d[0].foodtype)
    return render(request,'viewdonationrequest.html',{'name':name,'list':d})
# ---------------------------------------------------------------------------------
def gallery(request):
    name=request.session.get('name',default='Guest')
    return render(request,'gallery.html',{'name':name})

def ngopage(request):
    name=request.session.get('name',default='Guest')
    return render(request,'ngopage.html',{'name':name})


def ngodetail(request):
    name=request.session.get('name',default='Guest')
    return render(request,'ngodetails.html',{'name':name})
def userdetail(request):
    name=request.session.get('name',default='Guest')
    return render(request,'userdetails.html',{'name':name})


def about(request):
    name=request.session.get('name',default='Guest')
    return render(request,'about.html',{'name':name})
def aboutuser(request):
    name=request.session.get('name',default='Guest')
    return render(request,'aboutuser.html',{'name':name})
def aboutngo(request):
    name=request.session.get('name',default='Guest')
    return render(request,'aboutngo.html',{'name':name})

def contact(request):
    name=request.session.get('name',default='Guest')
    return render(request,'contact.html',{'name':name})
def contactuser(request):
    name=request.session.get('name',default='Guest')
    return render(request,'contactuser.html',{'name':name})
def contactngo(request):
    name=request.session.get('name',default='Guest')
    return render(request,'contactngo.html',{'name':name})

def HomePage(request):
    name=request.session.get('name',default='Guest')
    return render(request,'home.html',{'name':name})

def homeuser(request):
    name=request.session.get('name',default='Guest')
    return render(request,'homeuser.html',{'name':name})
def homengo(request):
    name=request.session.get('name',default='Guest')
    return render(request,'homengo.html',{'name':name})

# ------------------------------------------------------------------------------
# for all users
def userBase(request):
    return render(request,'userBase.html')

# ------------------------------------------------------------------------------
# for  doner users
def users(request):
    name=request.session.get('name',default='Guest')
    return render(request,'users.html',{'name':name})
# ------------------------------------------------------------------------------
# for  ngo
def ngoBase(request):
    return render(request,'ngoBase.html')

# -----------------------------------------------------------------------------------
def changepassword(request):
    name=request.session.get('name',default='Guest')
    # return render(request,'changepassword.html',{'name':name})
    if request.method=='POST':
        Currentpassword=request.POST['cpassword']
        Newpassword=request.POST['npassword']
        Confirmpassword=request.POST['cnpassword']
        # User = get_user_model()
        p1 = myUser.objects.all()
        for i in p1:
            if i.password==Currentpassword:
                i.password = Newpassword
                messages.info(request, 'password successfully changed')
            else:    
                messages.info(request, 'Inavlid Username/Password')
        return render(request,'changepassword.html')    
        
    else:
        return render(request,'changepassword.html')
# def managegallary():
#     image1 = request.POST[im]
    
