from rest_framework import serializers

from drf.models import ReportsImage, Reports, Merch
from drf.models.activity import OurActivity, TextActivity
from drf.models.donate import Donate
from drf.models.hero import Section
from drf.models.photo import Photo
from drf.models.support import Support
from drf.models.temmate import Teammate


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


class TextAvtivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextActivity
        fields = ['id', 'text_uk', 'text_en']


class ActivitySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    text = TextAvtivitySerializer(many=True, read_only=True)

    class Meta:
        model = OurActivity
        fields = ['id', 'text', 'photos']


class DonateSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Donate
        fields = ['id', 'text_uk', 'text_en', 'goal_uk', 'goal_en', 'donata_link', 'photos']


class ReportsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsImage
        fields = ['id', 'title_uk', 'title_en', 'quantity', 'image']


class ReportsSerializer(serializers.ModelSerializer):
    photos = ReportsImageSerializer(many=True, read_only=True)

    class Meta:
        model = Reports
        fields = ['id', 'text_uk', 'text_en', 'photos']


class MerchSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Merch
        fields = ['id', 'text_uk', 'text_en', 'photos']


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = ['id', 'name_uk', 'name_en', 'link', 'logo']
