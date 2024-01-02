from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models.hero import Section
from drf.serializers import SectionSerializer


class HeroView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Section.objects.first()
        serializer = SectionSerializer(queryset)
        return Response(serializer.data)