from django.contrib import admin
from .models import expendature

class expendatureAdmin(admin.ModelAdmin):
  list_display = ('Reciept_No', 'Amount','Purpose')
  list_display_links = ('Reciept_No',)
  
admin.site.register(expendature, expendatureAdmin)