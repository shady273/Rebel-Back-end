from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models import Merch
from drf.serializers import MerchSerializer


class MerchView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Merch.objects.first()
        serializer = MerchSerializer(queryset, context={'request': request})
        return Response(serializer.data)