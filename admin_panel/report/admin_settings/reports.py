from drf.admin_settings.base import BaseInline
from report.admin_settings.base import BaseAdmin
from report.models import Items


class ReportsItemInline(BaseInline):
    model = Items


class ReportsAdmin(BaseAdmin):
    inlines = [ReportsItemInline]
