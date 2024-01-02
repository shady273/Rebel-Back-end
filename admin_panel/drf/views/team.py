from rest_framework.generics import ListCreateAPIView

from drf.models.temmate import Teammate
from drf.serializers import TeamSerializer


class TeamListView(ListCreateAPIView):
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer