from django.contrib import admin

from drf.models.activity import OurActivity, TextActivity
from drf.models.donate import Donate
from drf.models.hero import Section
from drf.models.photo import Photo
from drf.models.temmate import Teammate


class SectionPhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    fk_name = 'section'
    exclude = ['activity']


class SectionAdmin(admin.ModelAdmin):
    inlines = [SectionPhotoInline]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


admin.site.register(Section, SectionAdmin)


class TextActivityInline(admin.StackedInline):
    model = TextActivity
    extra = 1
    fk_name = 'text_activity'
    exclude = ['section']


class ActivityPhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    fk_name = 'activity'
    exclude = ['section']


class ActivityAdmin(admin.ModelAdmin):
    inlines = [TextActivityInline, ActivityPhotoInline]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


admin.site.register(OurActivity, ActivityAdmin)


class DonatePhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    exclude = ['activity', 'section']


class DonateAdmin(admin.ModelAdmin):
    inlines = [DonatePhotoInline]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


admin.site.register(Donate, DonateAdmin)

admin.site.register(Teammate)

admin.site.site_title = 'Rebel Адміністрування'
admin.site.site_header = 'Rebel Адміністрування'
