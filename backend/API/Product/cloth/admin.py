from django.contrib import admin
from . models import sales


# Register your models here.
# admin.site.register(sales)
@admin.register(sales)
class salesAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','description']
    
    list_filter = ('category', 'price')
    
    search_fields: ['name']
    