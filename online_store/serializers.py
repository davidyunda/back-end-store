from rest_framework import serializers;
from .models import PhotoModel

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('id', 'name', 'price', 'photo')




