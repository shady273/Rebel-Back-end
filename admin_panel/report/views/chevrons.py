from rest_framework.generics import ListAPIView

from report.models.chevrons import ChevronPhoto
from report.serializers import ChevronsSerializer


class ChevronListView(ListAPIView):
    queryset = ChevronPhoto.objects.all()
    serializer_class = ChevronsSerializer