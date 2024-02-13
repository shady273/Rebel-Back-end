from rest_framework.generics import ListAPIView

from report.models import AllReports
from report.serializers import ReportsSerializer


class ReportsView(ListAPIView):
    queryset = AllReports.objects.all()
    serializer_class = ReportsSerializer