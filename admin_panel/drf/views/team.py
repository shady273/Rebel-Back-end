from rest_framework.generics import ListAPIView

from drf.models.temmate import Teammate
from drf.serializers import TeamSerializer


class TeamListView(ListAPIView):
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer
