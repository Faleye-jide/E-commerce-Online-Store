from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ['name', 'id']
    
admin.site.register(Item, ItemAdmin)

# Add this it change the header of the admin panel. 
admin.site.site_header = 'Items Admin'

admin.site.index_title = 'Items Store'