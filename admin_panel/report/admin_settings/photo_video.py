from drf.admin_settings.base import BaseInline, BaseAdmin
from report.models import Photo, Video


class ReportsPhotoInline(BaseInline):
    model = Photo


class ReportsVideoInline(BaseInline):
    model = Video


class ReportsPVAdmin(BaseAdmin):
    inlines = [ReportsPhotoInline, ReportsVideoInline]