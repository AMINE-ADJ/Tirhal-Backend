from rest_framework import serializers
from .models import Utilizer

class UtilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilizer
        fields= "__all__"