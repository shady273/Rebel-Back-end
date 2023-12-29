from rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = ['id', 'name_uk', 'name_en', 'role_uk', 'role_en', 'insta_link', 'image_data']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']


class SectionSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'text_uk', 'text_en', 'photos']
