"""
URL configuration for admin_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf.views.avtivity import ActivityView
from drf.views.donate import DonateView
from drf.views.hero import HeroView
from drf.views.team import TeamListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/team/', TeamListView.as_view(), name='team'),
    path('api/hero/', HeroView.as_view(), name='hero'),
    path('api/activity/', ActivityView.as_view(), name='activity'),
    path('api/donate/', DonateView.as_view(), name='activity'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
