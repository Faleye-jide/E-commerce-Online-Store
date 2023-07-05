from django.urls import path
from django.conf.urls import url
from . views import list_sales, create_sale, update_sale, delete_sale

urlpatterns = [
    path('', list_sales, name ='list_sales'),
    path('create', create_sale, name ='create_sale'),
    path('update/<int:id>/', update_sale, name ='update_sale'),
    path('delete/<int:id>/', delete_sale, name='delete'),
    
]
