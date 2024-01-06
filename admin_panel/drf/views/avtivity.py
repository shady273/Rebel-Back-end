from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models.activity import OurActivity
from drf.serializers import ActivitySerializer


class ActivityView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = OurActivity.objects.first()
        serializer = ActivitySerializer(queryset, context={'request': request})
        return Response(serializer.data)
