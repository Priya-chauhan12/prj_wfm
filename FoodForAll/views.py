
from ast import If
from copyreg import pickle
from email.policy import default
from re import U
from statistics import quantiles
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.template import context
from django.db.models import Sum
from pymysql import NULL
from FoodForAll.models import cartItem, feedback, fooddata, foodpack, myUser,cart, packCart
from FoodForAll.models import donation,userdetail



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
        fullname = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        phoneno = request.POST.get('phone', '')
        aadhar = request.POST.get('aadhar', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        usertype = 'doner'
        print(password1)
        print(password2)
        if password1 == password2:
            user = User(password=password1, username=username, email=email)
            user.save()
            alluser = myUser(username=username, email=email,
                             password=password1, usertype=usertype)
            alluser.save()
            doner=userdetail(fullname=fullname,phoneno=phoneno,aadhar=aadhar,address=address,
            city=city,state=state,zip=zip,user=alluser)
            doner.save()
            request.session['name'] = username
            messages.info(request, 'Register successfully..!')
            return redirect('login')     
        else:
            messages.info(request, 'dont match password')
            return redirect('donerregister')

    else:
        return render(request, 'donerregister.html')
# ----------------------------------------------------------------
def consumerregister(request):
    # request.session['name'] = username
    if request.method == "POST":
        username = request.POST.get('username', '')
        fullname = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        phoneno = request.POST.get('phone', '')
        aadhar = request.POST.get('aadhar', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        usertype = 'consumer'
        if password1 == password2:
            user = User(password=password1, username=username, email=email)
            user.save()
            alluser = myUser(username=username, email=email,
                             password=password1, usertype=usertype)
            alluser.save()
            consumer=userdetail(fullname=fullname,phoneno=phoneno,aadhar=aadhar,address=address,
            city=city,state=state,zip=zip,user=alluser)
            consumer.save()
            userCart=cart(user=consumer)
            userCart.save()
            
            messages.info(request, 'Register successfully..!')
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
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    if request.method == "POST": 
        foodtype = request.POST.get('foodtype', '')
        quantity = request.POST.get('quantity', '')
        dateofc = request.POST.get('dateofc', '')
        timeofc = request.POST.get('timeofc', '')
        address = request.POST.get('address', '')
        status='panding'
        user=user
        d = donation(user=user, foodtype=foodtype, quantity=quantity,
                        status=status,dateofc=dateofc, timeofc=timeofc, address=address)
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
    # id = request.session.get('id')
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    df=list(donation.objects.filter(user=user))
    
    return render(request, 'requeststatus.html', {'name': name,'list':df})
#----------------------------------------------------------------------------------

def confirm(request):
    name = request.session.get('name', default='Guest')
    if request.method == "POST":
        fid=request.POST.get('fid', '')
        fd=donation.objects.get(id=fid)
        fd.status="confirm"
        fd.save()
        x=fd.foodtype
        y=fd.quantity
        print(x)
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
        foodQuantity=request.POST.get('foodq', '')
        print(foodQuantity)
        AvailableFood=fooddata.objects.get(foodtype=foodtype)
        foodtype=AvailableFood
        AvailableFoodQuantity=AvailableFood.quantity
        if AvailableFoodQuantity >=int(foodQuantity):
            id=myUser.objects.get(username=name)
            user=userdetail.objects.get(user=id)
            c=cart.objects.get(user=user)
            ci=cartItem(foodtype=foodtype,quantity=foodQuantity,cart=c)
            ci.save()
            messages.info(request, 'Added to Cart..!')
        else:
            
            messages.error(request, 'Not Available..!')
        return redirect('selectfood')
    return render(request, 'select.html', {'name': name,'food':AvailableFood})
# ------------------------------------------------------------------------------------
def selectpack(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    if request.method == "POST":
        packQuantity=request.POST.get('packq','')
        pack=request.POST.get('foodpack', '')
        AvailableFoodPack=(foodpack.objects.get(packName=pack))
        FoodPack=AvailableFoodPack
        id=myUser.objects.get(username=name)
        user=userdetail.objects.get(user=id)
        c=cart.objects.get(user=user)
        ci=packCart(foodpack=FoodPack ,quantity=packQuantity,cart=c)
        ci.save()
        return redirect('selectfood')
    return render(request, 'select.html', {'name': name})
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
    food=list(fooddata.objects.all())
    foodPack=list(foodpack.objects.all())
    return render(request, 'selectfood.html', {'name': name,'list':food,'foodPack':foodPack})


#--------------------------------------------------------------------------------------
def mycart(request):
    name = request.session.get('name', default='Guest')
    # id=request.session['id']
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    c=cart.objects.get(user=user)
    ci=list(cartItem.objects.filter(cart=c,status='Pending'))
    pi=list(packCart.objects.filter(cart=c,status='Pending'))
    
    return render(request, 'mycart.html', {'name': name,'cartItem':ci,'cart':c,'foodpack':pi})
#--------------------------------------------------------------------------------------

def order(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    if request.method == "POST":
        cartId=request.POST.get('cartID', '')
        foodpackList=packCart.objects.filter(cart=cartId)
        MyCartList=cartItem.objects.filter(cart=cartId)
        for x in foodpackList:
            x.status='send'
            x.save()
        for x in MyCartList:
            x.status='send'
            x.save()
       
        messages.error(request, 'Your order has been placed..!')
        # cartItem.objects.filter(cart=c).delete()
        # packCart.objects.filter(cart=c).delete()
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
    if request.method == "POST":
        foodtype=request.POST.get('foodtype', '')
        AvailableFood=fooddata.objects.get(foodtype=foodtype)
        c=cart.objects.get(user=id)
        cartItem.objects.filter(cart=c,foodtype=AvailableFood).delete()
        return redirect('mycart')
    return render(request, 'removeall.html', {'name': name})

def remove1(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    if request.method == "POST":
        pack=request.POST.get('foodpack', '')
        AvailableFoodPack=foodpack.objects.get(packName=pack)
        c=cart.objects.get(user=id)
        packCart.objects.filter(cart=c,foodpack=AvailableFoodPack).delete()
        return redirect('mycart')
    return render(request, 'removeall.html', {'name': name})

# ---------------------------------------------------------------------
def removeall(request):
    name = request.session.get('name', default='Guest')
    id=request.session['id']
    c=cart.objects.get(user=id)
    cartItem.objects.filter(cart=c).delete()
    packCart.objects.filter(cart=c).delete()
    return redirect('mycart')
    # return render(request, 'removeall.html', {'name': name})



# ---------------------------------------------------------------------
def foodrequest(request):
    name = request.session.get('name', default='Guest')
    foodOrder=cartItem.objects.filter(status='send')
    packOrder=packCart.objects.filter(status='send')
    
    context={
        'foodOrder':foodOrder,
        'packOrder':packOrder,
        'name': name,
    }
    return render(request, 'foodrequest.html',context)
# --------------------------------------------------------------------
def foodConfirm(request):
    name = request.session.get('name', default='Guest')
    if request.method == "POST":
        fid=request.POST.get('fid', '')
        foodItem=cartItem.objects.get(id=fid)
        foodId=foodItem.foodtype.id
        availableFood=fooddata.objects.get(id=foodId)
        availableQuantity=availableFood.quantity
        requiredQuantity=foodItem.quantity
        if int(availableQuantity)>=int(requiredQuantity):
            availableFood.quantity-=int(requiredQuantity)
            availableFood.save()
            foodItem.status="confirm"
            foodItem.save()
    return render(request, 'ngopage.html', {'name': name})
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

def cabout(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'cabout.html', {'name': name})
def ccontact(request):
    name = request.session.get('name', default='Guest')
    return render(request, 'ccontact.html', {'name': name})

def updateprf(request):
    name = request.session.get('name', default='Guest')
    user=myUser.objects.get(username=name)
    us=userdetail.objects.get(user=user)
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        fullname = request.POST.get('fullname', '')
        phoneno = request.POST.get('phoneno', '')
        address = request.POST.get('address', '')
        aadhar = request.POST.get('aadhar', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        if(len(username) != 0):
            user.username=username
        if(len(email) != 0):
            user.email=email
        if(len(fullname) != 0):
            us.fullname=fullname
        if(len(phoneno) != 0):
            us.phoneno=phoneno  
        if(len(address) != 0):
            us.address=address
        if(len(aadhar) != 0):
            us.aadhar=aadhar
        if(len(city) != 0):
            us.city=city
        if(len(state) != 0):
            us.state=state
        if(len(zip) != 0):
            us.zip=zip                
        user.save()
        us.save()
        if user.usertype == 'ngo':
            return redirect('ngopage')
        elif user.usertype=='doner':
            return redirect('users')
        else:
            return redirect('consumer')
    return render(request, 'updateprf.html', {'name': name, 'user':user,'us':us})        


def changepassword(request):
    name = request.session.get('name', default='Guest')
    user=myUser.objects.get(username=name)
    if request.method == "POST":
        cpassword = request.POST.get('cpassword', '')
        npassword = request.POST.get('npassword', '')
        cnpassword = request.POST.get('cnpassword', '')
        currentPassword=user.password
        if currentPassword==cpassword:
            if npassword==cnpassword:
                user.password=npassword
                user.save()
                messages.error(request, 'Password Successfuly changed.....!')
                return redirect('login')
            else:
                messages.error(request, "Password dosen't match....!")
                redirect('changepassword')
        else:
            messages.error(request, 'Provide correct password.')
            redirect('changepassword')
    return render(request, 'changepassword.html', {'name': name})

# ------------------------------------------------------------
def listdoner(request):
    name = request.session.get('name', default='Guest')
    d=list(donation.objects.filter(status='confirm')) 
    return render(request,'listdoner.html',{'name': name,'list':d})
# -------------------------------------------------------------
def predonation(request):
    name = request.session.get('name', default='Guest')
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    df=list(donation.objects.filter(user=user,status='confirm'))
    return render(request,'predonation.html',{'name': name,'list':df})
# -------------------------------------------------------------
def previousOrder(request):
    name = request.session.get('name', default='Guest')
    # id=request.session['id']
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    myCart=cart.objects.get(user=user)
    cartID=myCart.id
    cartItems=cartItem.objects.filter(cart=cartID , status="send")
    Items=cartItem.objects.filter(cart=cartID , status="confirm")
    context={
        'item':cartItems,
        'j':Items,
        'name': name
    }
    
    return render(request, 'previousOrder.html',context)

# -------------------------------------------------------------------
def viewfeedback(request):
    name = request.session.get('name', default='Guest')
    f=list(feedback.objects.all())
    return render(request, 'viewfeedback.html', {'name': name,'list':f})


def feedbackinfo(request):
    name=request.session.get('name',default='Guest')
    id=myUser.objects.get(username=name)
    user=userdetail.objects.get(user=id)
    if request.method == "POST":
       desc=request.POST.get('desc','')
       pic = request.FILES.get('pic','')
       user=user
       f = feedback(desc=desc, pic=pic, user=user)
       f.save()
       messages.error(request, 'Your feedback has been submited. Thank You....!')
       return redirect('consumer')
    else:
        return render(request, 'feedbackinfo.html',{'name':name})