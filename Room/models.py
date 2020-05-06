from django.db import models
from floor.models import floor
class room(models.Model):
    floor = models.ForeignKey(floor, on_delete=models.CASCADE)
    Room_NO = models.CharField(max_length=10)
    No_of_Beds = models.IntegerField()
    No_of_Person_Allowed = models.IntegerField()
    Charges_Per_Person = models.IntegerField()
    AC_Availability = models.BooleanField(default=True)
    Electricity = models.BooleanField(default=True)
    UPS = models.BooleanField(default=True)
    Description = models.TextField(blank=True)

    def __str__(self):
        return self.Room_NO
