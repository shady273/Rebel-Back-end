from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models.donate import Donate
from drf.serializers import DonateSerializer


class DonateView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Donate.objects.first()
        serializer = DonateSerializer(queryset)
        return Response(serializer.data)
