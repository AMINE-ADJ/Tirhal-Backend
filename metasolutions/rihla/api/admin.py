from django.contrib import admin
from .models import Utilizer,Region,Image,Place,Favorite,Comment,Rating,Transport,Event
modellist=[Utilizer,Region,Image,Place,Favorite,Comment,Rating,Event,Transport]
admin.site.register(modellist)

