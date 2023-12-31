from drf.admin_settings.base import BaseInline, PaginatedInline, BaseAdmin
from drf.models import Reports, ReportsImage


class ReportsImageInline(BaseInline):
    model = ReportsImage


class ReportsAdmin(BaseAdmin):
    inlines = [ReportsImageInline]
