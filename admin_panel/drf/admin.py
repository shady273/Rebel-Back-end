from django.contrib import admin

from drf.admin_settings.activity import ActivityAdmin
from drf.admin_settings.donate import DonateAdmin
from drf.admin_settings.hero import SectionAdmin
from drf.admin_settings.merch import MerchAdmin
from drf.admin_settings.quick_donate import QuickDonateAdmin
from drf.admin_settings.reports import ReportsAdmin
from drf.admin_settings.support import SupportAdmin
from drf.models import Reports, Merch
from drf.models.activity import OurActivity
from drf.models.donate import Donate
from drf.models.hero import Section
from drf.models.quick_donate import QuickDonate
from drf.models.support import Support
from drf.models.temmate import Teammate

admin.site.register(Section, SectionAdmin)

admin.site.register(OurActivity, ActivityAdmin)

admin.site.register(Donate, DonateAdmin)

admin.site.register(Reports, ReportsAdmin)

admin.site.register(Merch, MerchAdmin)

admin.site.register(Teammate)

admin.site.register(Support, SupportAdmin)

admin.site.register(QuickDonate, QuickDonateAdmin)

admin.site.site_title = 'Rebel Адміністрування'
admin.site.site_header = 'Rebel Адміністрування'
