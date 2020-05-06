from django.contrib import admin
from .models import room

class roomAdmin(admin.ModelAdmin):
  list_display = ('floor', 'Room_NO','No_of_Beds','No_of_Person_Allowed','AC_Availability','Electricity','UPS','Description')
  list_display_links = ('floor', 'Room_NO','No_of_Beds','No_of_Person_Allowed','AC_Availability','Electricity','UPS')
  
admin.site.register(room, roomAdmin)
