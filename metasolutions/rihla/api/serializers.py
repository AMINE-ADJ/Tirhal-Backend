from rest_framework import serializers
from .models import Utilizer,Region,Place,Image,Favorite,Feedback

class UtilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilizer
        fields= "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
class MiniPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields=('id','latitude','longitude')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields='__all__'