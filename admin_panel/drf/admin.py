from django.contrib import admin
from .models import *


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


admin.site.register(Section, SectionAdmin)
admin.site.register(Teammate)

admin.site.site_title = 'Rebel Адміністрування'
admin.site.site_header = 'Rebel Адміністрування'
