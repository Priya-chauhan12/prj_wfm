
from copyreg import pickle
from email.policy import default
from statistics import quantiles
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.template import context
from django.db.models import Sum
from pkg_resources import AvailableDistributions
from FoodForAll.models import cartItem, fooddata, myUser,cart,feedback
from FoodForAll.models import donation,userdetail
from FoodForAll.forms import uploadinfo

# ------------------------------------------------------------------------------
# for login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # User = get_user_model()
        users = myUser.objects.all()
        for i in users:
            if i.username == username and i.password == password:
                request.session['name'] = username
                request.session['id']=i.id
                usertype = i.usertype
                if usertype == 'ngo':
                    return redirect('ngopage')
                elif usertype=='doner':
                    return redirect('users')
                else:
                     return redirect('consumer')
        messages.info(request, 'Inavlid Username/Password')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

# ----------------------------------------------------------------------------------------
# for registration


def registerview(request):
    return render(request, 'register.html')


def register(request):
    return render(request, 'register.html')
# ------------------------------------------------------------------------------


def ngoregister(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        usertype = 'ngo'
        if password1 == password2:
            user = User(password=password1, username=username, email=email)
            user.save()
            alluser = myUser(username=username, email=email,
                             password=password1, usertype=usertype)
            alluser.save()
            request.session['name'] = username
            messages.info(request, 'Register successfully..!')
            return redirect('ngopage')
           
        else:
            messages.info(request, 'dont match password')
            return redirect('ngoregister')

    else:
        return render(request, 'ngoregister.html')
# ------------------------------------------------------------------------------

def donerregister(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        usertype = 'doner'
        if password1 == password2:
            user = User(password=password1, username=username, email=email)
            user.save()
            alluser = myUser(username=username, email=email,
                             password=password1, usertype=usertype)
            alluser.save()
            request.session['name'] = username
            messages.info(request, 'Register successfully..!')
            return redirect('users')     
        else:
            messages.info(request, 'dont match password')
            return redirect('donerregister')

    else:
        return render(request, 'donerregister.html')
# ----------------------------------------------------------------
def consumerregister(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        usertype = 'consumer'
        if password1 == password2:
            user = User(password=password1, username=username, email=email)
            user.save()
            alluser = myUser(username=username, email=email,
                             password=password1, usertype=usertype)
            alluser.save()
            request.session['name'] = username
            c=cart(user=alluser)
            c.save()
            return redirect('login')
           
        else:
            messages.info(request, 'dont match password')
            return redirect('consumerregister')

    else:
        return render(request, 'consumerregister.html')


def registration(request):
    return render(request, 'registration.html')


def consumer(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'consumer.html',{'name':name})
# for logout
def feedbackinfo(request):
    if request.method == "POST":
        form = uploadinfo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj=form.instance
            return render(request, 'feedbackinfo.html',{'form':form,'img_obj':img_obj})    
    else:
            form = uploadinfo()
    return render(request, 'feedbackinfo.html',{'form':form})
def listdoner(request):
    name = request.session.get('name', default='Guest')
    d=list(donation.objects.filter(status='confirm')) 
    return render(request,'listdoner.html',{'name': name,'list':d})
def logout(request):
    if 'name' in request.session['name']:
        print('name')
        del request.session['name']

    return redirect('login')
# --------------------------------------------------------------------------------
def donate(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'donate.html', {'name': name})

def donatefood(request):
    name=request.session.get('name',default='Guest')
    user=myUser.objects.get(username=name)
    if request.method == "POST": 
        foodtype = request.POST.get('foodtype', '')
        quantity = request.POST.get('quantity', '')
        dateofc = request.POST.get('dateofc', '')
        timeofc = request.POST.get('timeofc', '')
        address = request.POST.get('address', '')
        image=request.POST.get('image','')
        status='panding'
        user=user
        d = donation(user=user, foodtype=foodtype, quantity=quantity,
                        status=status,dateofc=dateofc, timeofc=timeofc, address=address,image=image)
        d.save()
        return redirect('users')
    else:
        return render(request, 'donatefood.html')

# ---------------------------------------------------------------------------------


def viewdonationrequest(request):
    name = request.session.get('name', default='Guest')
    d = list(donation.objects.filter(status='panding'))
    return render(request, 'viewdonationrequest.html', {'name': name, 'list': d})
# ---------------------------------------------------------------------------------
def requeststatus(request):
    name = request.session.get('name', default='Guest')
    id = request.session.get('id')
    df=list(donation.objects.filter(user=id))
    return render(request, 'requeststatus.html', {'name': name,'list':df})
#----------------------------------------------------------------------------------
def predonation(request):
    name = request.session.get('name', default='Guest')
    id = request.session.get('id')
    df=list(donation.objects.filter(user=id,status='confirm'))
    return render(request,'predonation.html',{'name': name,'list':df})
def confirm(request):
    name = request.session.get('name', default='Guest')
    if request.method == "POST":
        fid=request.POST.get('fid', '')
        fd=donation.objects.get(id=fid)
        fd.status="confirm"
        fd.save()
        x=fd.foodtype
        y=fd.quantity
        f=fooddata.objects.get(foodtype=x)
        f.quantity+=y
        f.available=True
        f.save()
        return redirect('viewdonationrequest')
    return render(request, 'confirm.html', {'name': name})

def cancel(request):
    name = request.session.get('name', default='Guest')
    if request.method == "POST":
        fid=request.POST.get('fid', '')
        fd=donation.objects.get(id=fid)
        fd.status="cancel"
        fd.save()
    return render(request, 'cancel.html', {'name': name})


# ------------------------------------------------------------------------------------
def select(request):
    name = request.session.get('name', default='Guest')
    if request.method == "POST":
        id=request.session['id']
        foodtype=request.POST.get('foodtype', '')
        quan=request.POST.get('qu','')
        AvailableFood=fooddata.objects.get(foodtype=foodtype)
        foodtype=AvailableFood
        AvailableFoodQuantity=AvailableFood.quantity
        if AvailableFoodQuantity>=int(quan):
            AvailableFood.message=False
            AvailableFood.save()
            c=cart.objects.get(user=id)
            ci=cartItem(foodtype=foodtype,quantity=quan,cart=c)
            ci.save()
        else:
            AvailableFood.message=True
            AvailableFood.save()
            messages.error(request, 'Not available this much of quantity please select other.Available quantity:')
        return redirect('selectfood')
    return render(request, 'select.html', {'name': name,'food':AvailableFood})

#--------------------------------------------------------------------------------------
def afood(request):
    name = request.session.get('name', default='Guest')
    # d = (donation.objects
    # .values('foodtype')
    # .annotate(quantity=Sum('quantity'))
    # .order_by()).filter(status='confirm')
    d=list(fooddata.objects.all())
    return render(request, 'afood.html', {'name': name,'list':d})


#--------------------------------------------------------------------------------------
def selectfood(request):
    name = request.session.get('name', default='Guest')
    d=list(fooddata.objects.all())
    return render(request, 'selectfood.html', {'name': name,'list':d})


#--------------------------------------------------------------------------------------
def mycart(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    c=cart.objects.get(user=id)
    ci=list(cartItem.objects.filter(cart=c))
    return render(request, 'mycart.html', {'name': name,'cartItem':ci,'cart':c})
#--------------------------------------------------------------------------------------

def order(request):
    name = request.session.get('name', default='Guest')
    # AvailableFood=list(fooddata.objects.all())
    if request.method == "POST":
        cartId=request.POST.get('cartID', '')
        # MyCartList=list(cartItem.objects.filter(cart=cartId))
        MyCartList=(cartItem.objects.filter(cart=cartId))
    
        print(MyCartList)
        
            
        return redirect('mycart')
    return render(request, 'order.html', {'name': name})

# ---------------------------------------------------------------------
def confirmOrder(request):
    name = request.session.get('name', default='Guest')
    AvailableFood=fooddata.objects.all()
    print(AvailableFood)
    return render(request, 'confirm.html', {'name': name})
# ---------------------------------------------------------------------
def remove(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    # if request.method == "POST":
        # c=cart.objects.get(user=id)
        # cartItem.objects.filter(cart=c).delete()
        # return redirect('mycart')
    return render(request, 'removeall.html', {'name': name})
# ---------------------------------------------------------------------
def removeall(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    c=cart.objects.get(user=id)
    cartItem.objects.filter(cart=c).delete()
    return redirect('mycart')
    # return render(request, 'removeall.html', {'name': name})

# ---------------------------------------------------------------------
def gallery(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'gallery.html', {'name': name})
def ngopage(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'ngopage.html', {'name': name})


def ngodetail(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'ngodetails.html', {'name': name})


def userdetails(request):
    name=request.session.get('name',default='Guest')
    user=myUser.objects.get(username=name)
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST.get('lastname', '')
        gender = request.POST.get('gender', '')
        phoneno = request.POST.get('phoneno', '')
        bdate = request.POST.get('bdate', '')
        aadhar = request.POST.get('aadhar', '')
        address = request.POST.get('address', '')
        user=user
        ud=userdetail(user=user,firstname=firstname,lastname=lastname,gender=gender,
        phoneno=phoneno,bdate=bdate,address=address,aadhar=aadhar)
        ud.save()
        return redirect('login')
    return render(request, 'userdetails.html', {'name': name})


def about(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'about.html', {'name': name})


def aboutuser(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'aboutuser.html', {'name': name})


def aboutngo(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'aboutngo.html', {'name': name})


def contact(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'contact.html', {'name': name})


def contactuser(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'contactuser.html', {'name': name})


def contactngo(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'contactngo.html', {'name': name})


def HomePage(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'home.html', {'name': name})


def homeuser(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'homeuser.html', {'name': name})


def homengo(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'homengo.html', {'name': name})

# ------------------------------------------------------------------------------
# for all users


def userBase(request):
    return render(request, 'userBase.html')

# ------------------------------------------------------------------------------
# for  doner users


def users(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'users.html', {'name': name})
# ------------------------------------------------------------------------------
# for  ngo


def ngoBase(request):
    return render(request, 'ngoBase.html')

# -----------------------------------------------------------------------------------
def chome(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'chome.html', {'name': name})
def cabout(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'cabout.html', {'name': name})
def ccontact(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'ccontact.html', {'name': name})



def changepassword(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'changepassword.html', {'name': name})
