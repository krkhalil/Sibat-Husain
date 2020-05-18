from django.contrib import admin
from .models import payment
from .models import renter

class paymentAdmin(admin.ModelAdmin):
  list_display = ('Renter_Name','Recepit_No','Amount','Paying_Date','Fine_Charges','Room_Rent','Room_Servece','Food_Charges','Internet_Charges','Convance_Charges','Laundary_Charges','Other_Charges','Description')
  list_display_links = ('Renter_Name',)
  list_per_page = 25
  fields = (('Renter_Name','Recepit_No','Amount'),('Paying_Date'),('Room_Rent','Room_Servece','Fine_Charges','Food_Charges','Internet_Charges','Convance_Charges','Laundary_Charges','Other_Charges'),'Description')
 
  
admin.site.register(payment, paymentAdmin)
