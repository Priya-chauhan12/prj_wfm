from django.contrib import admin



from .models import myUser,donatefoods


# # register model
admin.site.register(myUser)
admin.site.register(donatefoods)