from django.urls import path
from .views import ItemList, ItemDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('items', ItemList.as_view()),
    path('item-detail/<int:pk>', ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)