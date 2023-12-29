from rest_framework.generics import ListCreateAPIView

from drf.models import *
from drf.serializers import *


class TeamListView(ListCreateAPIView):
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer


class HeroListView(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
