from rest_framework import serializers
from .models import Teammate


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = ['name', 'role', 'insta_link', 'image_data']
