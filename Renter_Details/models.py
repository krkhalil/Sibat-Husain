from django.db import models
from datetime import datetime
from floor.models import floor
from Room.models import room
class renter(models.Model):
    Renter_Name = models.CharField(max_length=200)
    Father_Name = models.CharField(max_length=200)
    Renter_CNIC = models.CharField(max_length=200)

    Mobile_No = models.CharField(max_length=12)
    ICOE_No = models.CharField(max_length=12)

    Renter_Image_scan = models.ImageField(upload_to='photos/%Y/%m/%d/')


    Renter_CNIC_Image_scan = models.ImageField(upload_to='photos/%Y/%m/%d/')



    Floor = models.ForeignKey(floor, on_delete=models.CASCADE)
    Room = models.ForeignKey(room, on_delete=models.CASCADE)
    
    Renter_Profession = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    Tehseel = models.CharField(max_length=200)
    Complete_Address = models.CharField(max_length=500)

    Advance_payment = models.IntegerField(default=0)
    Checkin_Date = models.DateTimeField(default=datetime.now, blank=True)
    Expected_Checkout_Date = models.DateTimeField(default=datetime.now, blank=True)

    
    def __str__(self):
        return self.Renter_Name
