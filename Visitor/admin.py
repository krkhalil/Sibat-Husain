from django.contrib import admin
from .models import Visitor

class VisitorAdmin(admin.ModelAdmin):
  list_display = ('Renter_Name','Visitor_Name','Visitor_CNIC_NO','Take_In_Time','Take_Out_Time','Description')
  list_display_links = ('Renter_Name',)
  search_fields = ('Visitor_Name','Visitor_CNIC_NO',)
  list_per_page = 25
  
admin.site.register(Visitor, VisitorAdmin)

