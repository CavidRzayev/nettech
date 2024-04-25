from rest_framework import serializers
from .models import *

class ListBoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'


class ListRigsSerializers(serializers.ModelSerializer):
    box_rigs = ListBoxSerializers(many=True,read_only=True)
    class Meta:
        model = Rig
        fields = '__all__'


class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
