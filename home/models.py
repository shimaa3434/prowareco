from django.db import models

# Create your models here.
class Phone(models.Model):
    number = models.CharField(max_length=16)
    def __str__(self):
        return self.number
    

class Info(models.Model):
    place= models.CharField(max_length=200)
    phone= models.ForeignKey("Phone", on_delete=models.CASCADE)
    email= models.EmailField(max_length=254)

    def __str__(self):
        return self.place

class Service(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    dec= models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=254)
    phone = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    