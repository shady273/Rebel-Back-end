from django.contrib import admin

from report.admin_settings.photo_video import ReportsPVAdmin
from report.admin_settings.reports import ReportsAdmin
from report.models import Reports, ThanksPhoto
from report.models import ReportsPV
from report.models.chevrons import ChevronPhoto
from report.models.news import News

admin.site.register(Reports, ReportsAdmin)

admin.site.register(ReportsPV, ReportsPVAdmin)

admin.site.register(News)

admin.site.register(ThanksPhoto)

admin.site.register(ChevronPhoto)