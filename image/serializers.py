from django.shortcuts import render
from .models import Images
from rest_framework import serializers
from .serializers import *


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'