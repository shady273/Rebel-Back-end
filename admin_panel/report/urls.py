from django.urls import path

from report.views.acknowledgments import ThanksListView
from report.views.chevrons import ChevronListView
from report.views.news import NewsListView
from report.views.photo_video import ReportsPVView
from report.views.report import ReportsView

urlpatterns = [
    path('all_reports/', ReportsView.as_view(), name='all reports'),
    path('reports_photo_video/', ReportsPVView.as_view(), name='photo video'),
    path('news/', NewsListView.as_view(), name='news'),
    path('thanks/', ThanksListView.as_view(), name='thanks'),
    path('chevrons/', ChevronListView.as_view(), name='chevrons'),
]

