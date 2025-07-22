from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=25)
    email=models.EmailField()
    pwd=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    Phn=models.CharField(max_length=10)

class Event(models.Model):
    etype=models.CharField(max_length=40)
    eimage=models.ImageField()
    eprice=models.CharField(max_length=20)
    edes=models.CharField(max_length=300)

class Pay(models.Model):
    id=models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    cardnum=models.CharField(max_length=60)
    cvvnum=models.CharField(max_length=60)
    edate=models.CharField(max_length=60)
    userid=models.CharField(max_length=60)
    etype=models.CharField(max_length=60)
    eid=models.CharField(max_length=20, default='default_value')
    eprice=models.CharField(max_length=60)
    edes=models.CharField(max_length=60)









