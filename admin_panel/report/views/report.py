from rest_framework.generics import ListAPIView

from report.models import Reports
from report.serializers import ReportsSerializer


class ReportsView(ListAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer