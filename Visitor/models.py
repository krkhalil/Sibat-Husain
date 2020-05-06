from django.db import models
from datetime import datetime
from Renter_Details.models import renter
class Visitor(models.Model):
    Renter_Name = models.ForeignKey(renter, on_delete=models.CASCADE)
    Visitor_Name = models.CharField(max_length=50)
    Visitor_CNIC_NO = models.CharField(max_length=15)
    Take_In_Time = models.DateTimeField(default=datetime.now, blank=True)
    Take_Out_Time = models.DateTimeField(default=datetime.now, blank=True)
    Description = models.TextField(blank=True)
    def __str__(self):
        return self.Description
