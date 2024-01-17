from drf.admin_settings.base import BaseAdmin, BaseInline
from drf.models.quick_donate import QuickDonate


class QuickDonateAdmin(BaseAdmin):
    model = QuickDonate