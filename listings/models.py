from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    # ForeignKey makes relationships 
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) #DO_NOTHING so nothing happens incase you delete Realtor
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #blank=True makes it optional
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True) #blank=true makes it options

    def __str__(self):
        # returns the main field to be displayed which is title
        return self.title  