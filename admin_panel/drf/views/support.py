from rest_framework.generics import ListCreateAPIView

from drf.models.support import Support
from drf.serializers import SupportSerializer


class SupportListView(ListCreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer