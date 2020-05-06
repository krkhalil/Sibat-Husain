from django.contrib import admin
from .models import renter
from django.utils import timezone
from import_export.admin import ImportExportModelAdmin
class ViewAdmin(ImportExportModelAdmin):
      pass
class renterAdmin(admin.ModelAdmin):
  list_display = ('Renter_Name','Father_Name','Renter_CNIC','Mobile_No','ICOE_No','Expected_Checkout_Date','Remaining_days','Floor','Room','District','Tehseel','Complete_Address')
  list_display_links = ('Renter_Name',)
  search_fields = ('Renter_Name','Renter_CNIC',)
  list_per_page = 25
  fields = (('Renter_Name','Father_Name','Renter_CNIC'),('Mobile_No','ICOE_No'),('Floor','Room'),('District','Tehseel','Complete_Address'),('Renter_Image_scan','Renter_CNIC_Image_scan'),('Checkin_Date','Expected_Checkout_Date'))
  
  def Remaining_days(self,renter):
        remain =  renter.Expected_Checkout_Date - timezone.now()
        return remain.days
        



admin.site.register(renter, renterAdmin)

