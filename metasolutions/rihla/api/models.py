from django.db import models

# Create your models here.
class Utilizer(models.Model):
    email=models.CharField(max_length=255)
    role=models.CharField(max_length=255,default='touriste')
    password=models.CharField(max_length=63)
    firstname=models.CharField(max_length=63)
    lastname=models.CharField(max_length=63)
    def __str__(self):
        return self.firstname
