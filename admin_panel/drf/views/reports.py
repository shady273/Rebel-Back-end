from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models import Reports
from drf.serializers import ReportsSerializer


class ReportsView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Reports.objects.first()
        serializer = ReportsSerializer(queryset)
        return Response(serializer.data)
