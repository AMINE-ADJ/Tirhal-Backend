from django.db import models
from django.utils import timezone
# Create your models here.
class Utilizer(models.Model):
    email=models.CharField(max_length=255)
    role=models.CharField(max_length=255,default='touriste')
    password=models.CharField(max_length=63)
    fullname=models.CharField(max_length=63)
    # def __str__(self):
    #     return self.fullname
    
class Region(models.Model):
    wilaya=models.CharField(max_length=63)
    idUser=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True,blank=True)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)

class Place(models.Model):
    idRegion=models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    idUtilizer=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=63)
    category=models.CharField(max_length=63)
    theme=models.CharField(max_length=63,null=True,blank=True)
    description=models.TextField(max_length=4064,null=True,blank=True)
    latitude=models.FloatField()
    longitude=models.FloatField()
    datefrom=models.DateTimeField(null=True,blank=True)
    dateto=models.DateTimeField(null=True,blank=True)

class Image(models.Model):
    idPlace=models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='pictures',null=True,blank=True)
    link=models.CharField(max_length=512,null=True,blank=True)

class Favorite(models.Model):
    idUtilizer=models.ForeignKey(Utilizer,related_name='favorites', on_delete=models.CASCADE)
    idPlace=models.ForeignKey(Place,on_delete=models.CASCADE)

class Feedback(models.Model):
    idUtilizer=models.ForeignKey(Utilizer, on_delete=models.CASCADE)
    idPlace=models.ForeignKey(Place,related_name='feedbacks', on_delete=models.CASCADE)
    pubdate=models.DateTimeField(default=timezone.now())
    comment=models.TextField(blank=True,null=True,max_length=4064)
    rating=models.FloatField(null=True,blank=True)


    


