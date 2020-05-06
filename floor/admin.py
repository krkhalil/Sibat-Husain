from django.contrib import admin
from .models import floor

class floorAdmin(admin.ModelAdmin):
  list_display = ('name', 'NO_OF_Rooms')
  list_display_links = ('name', 'NO_OF_Rooms')
  
admin.site.register(floor, floorAdmin)

