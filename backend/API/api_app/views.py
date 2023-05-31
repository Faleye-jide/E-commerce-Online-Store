from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item
from rest_framework.throttling import UserRateThrottle
from .serializers import ItemSerializer

# Create your views here.

class ItemList(APIView):
    """
    List all the items or created a new item
    """
    # set the throttling policy on this class view
    throttle_classes = [UserRateThrottle]
    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ItemDetail(APIView):
    """
    Retrieve, update, or delete an item 
    """
    
    def get_object(self, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # return get_object_or_404(Item, pk=pk)
    
    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        print("ITEM", item)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        result = {
            "message":"deleted"
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)
    
    
class DeleteAllItems(APIView):
    
    def delete(self, request):

        Item.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
  
    