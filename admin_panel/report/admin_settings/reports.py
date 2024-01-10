from report.admin_settings.base import BaseInline, BaseAdmin
from report.models import Items


class ReportsItemInline(BaseInline):
    model = Items


class ReportsAdmin(BaseAdmin):
    inlines = [ReportsItemInline]
