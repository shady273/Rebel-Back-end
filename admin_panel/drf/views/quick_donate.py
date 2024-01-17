from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models.quick_donate import QuickDonate
from drf.serializers import QuickDonateSerializer


class QuickDonateView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = QuickDonate.objects.first()
        serializer = QuickDonateSerializer(queryset, context={'request': request})
        return Response(serializer.data)
