from rest_framework.response import Response
from rest_framework.views import APIView

from report.models.photo import ReportsPV
from report.serializers import ReportsPVSerializer


class ReportsPVView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ReportsPV.objects.first()
        serializer = ReportsPVSerializer(queryset, context={'request': request})
        return Response(serializer.data)
