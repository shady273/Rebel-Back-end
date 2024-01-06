from rest_framework.generics import ListAPIView

from drf.models.support import Support
from drf.serializers import SupportSerializer


class SupportListView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
