from re import U
from django.contrib import admin



from .models import myUser,donation,userdetail,cart,cartItem,fooddata


# # register model
admin.site.register(myUser)
admin.site.register(donation)
admin.site.register(userdetail)
admin.site.register(cart)
admin.site.register(cartItem)
admin.site.register(fooddata)