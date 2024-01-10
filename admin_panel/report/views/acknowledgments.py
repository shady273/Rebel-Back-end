from rest_framework.generics import ListAPIView

from report.models import ThanksPhoto
from report.serializers import ThanksSerializer


class ThanksListView(ListAPIView):
    queryset = ThanksPhoto.objects.all()
    serializer_class = ThanksSerializer
