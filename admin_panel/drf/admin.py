from django.contrib import admin

from drf.admin_settings.activity import ActivityAdmin
from drf.admin_settings.donate import DonateAdmin
from drf.admin_settings.hero import SectionAdmin
from drf.models.activity import OurActivity
from drf.models.donate import Donate
from drf.models.hero import Section
from drf.models.temmate import Teammate

admin.site.register(Section, SectionAdmin)

admin.site.register(OurActivity, ActivityAdmin)

admin.site.register(Donate, DonateAdmin)

admin.site.register(Teammate)

admin.site.site_title = 'Rebel Адміністрування'
admin.site.site_header = 'Rebel Адміністрування'
