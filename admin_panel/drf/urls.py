from django.urls import path

from drf.views.avtivity import ActivityView
from drf.views.donate import DonateView
from drf.views.hero import HeroView
from drf.views.merch import MerchView
from drf.views.quick_donate import QuickDonateView
from drf.views.reports import ReportsView
from drf.views.support import SupportListView
from drf.views.team import TeamListView

app_name = 'drf'

urlpatterns = [
    path('team/', TeamListView.as_view(), name='team'),
    path('hero/', HeroView.as_view(), name='hero'),
    path('activity/', ActivityView.as_view(), name='activity'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('merch/', MerchView.as_view(), name='merch'),
    path('support/', SupportListView.as_view(), name='support'),
    path('quick_donate/', QuickDonateView.as_view(), name='quick_donate'),

]
