from django.db import models
from Renter_Details.models import renter
from datetime import datetime
class payment(models.Model):
    Renter_Name = models.ForeignKey(renter, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Recepit_No = models.CharField(max_length=10)
    Room_Rent =  models.BooleanField(default=True)
    Room_Servece =  models.BooleanField(default=True)
    Food_Charges = models.BooleanField(default=True)
    Fine_Charges = models.BooleanField(default=True)
    Internet_Charges =  models.BooleanField(default=True)
    Convance_Charges = models.BooleanField(default=True)
    Laundary_Charges = models.BooleanField(default=True)
    Other_Charges = models.BooleanField(default=True)
    Paying_Date = models.DateTimeField(default=datetime.now, blank=True)
    Description = models.TextField(blank=True)

    def __str__(self):
        return self.Description
