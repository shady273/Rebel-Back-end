from rest_framework.generics import ListAPIView

from report.models.news import News
from report.serializers import NewsSerializer


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
