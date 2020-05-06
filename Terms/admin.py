from django.contrib import admin
from .models import term

class termAdmin(admin.ModelAdmin):
  list_display = ('Type_OF','Terms')
  list_display_links = ('Type_OF',)
  
admin.site.register(term, termAdmin)
