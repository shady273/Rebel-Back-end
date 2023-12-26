from rest_framework import serializers
from .models import Teammate


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = ['name_uk', 'name_en', 'role_uk', 'role_en', 'insta_link', 'image_data']
