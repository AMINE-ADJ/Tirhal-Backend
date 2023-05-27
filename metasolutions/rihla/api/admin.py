from django.contrib import admin
from .models import Utilizer,Region,Image,Place,Favorite,Feedback
modellist=[Utilizer,Region,Image,Place,Favorite,Feedback]
admin.site.register(modellist)

