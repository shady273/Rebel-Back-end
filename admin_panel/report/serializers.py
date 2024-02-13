from rest_framework import serializers

from report.models import Items, AllReports, ThanksPhoto
from report.models.chevrons import ChevronPhoto
from report.models.news import News
from report.models.photo import Photo, Video


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'title_uk', 'title_en', 'quantity']


class ReportsSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = AllReports
        fields = ['id', 'title_uk', 'title_en', 'items']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_url']


class ReportsPVSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)
    video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = AllReports
        fields = ['id', 'photo', 'video']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title_uk', 'title_en', 'text_uk', 'text_en', 'news_url', 'image']


class ThanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThanksPhoto
        fields = ['id', 'image']


class ChevronsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChevronPhoto
        fields = ['id', 'image']