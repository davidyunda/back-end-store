from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from .serializers import RoomSerializer
from .models import PhotoModel

from .models import PhotoModel

from rest_framework.decorators import api_view
from rest_framework.response import Response


class RoomView(generics.CreateAPIView):
    queryset = PhotoModel.objects.all()
    serializer_class = RoomSerializer

# Create your views here.
def home(request):
    page_name = 'Clothing Store'
    about = 'Website created by Django on:'
    menu_display = ['Men', 'Women', 'Sales', 'Shoes']
    product = PhotoModel.objects.all()
    return render(request, 'online_store/home.html', {'page_name':page_name, 'about':about, 'product':product})

@api_view(['GET'])
def getData(request):
    product = PhotoModel.objects.all()
    serializer = RoomSerializer(product, many=True)
    return Response(serializer.data)