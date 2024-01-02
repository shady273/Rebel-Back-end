from django.contrib import admin

from drf.admin_settings.base import BaseAdmin
from drf.models.photo import Photo


class SectionPhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    fk_name = 'section'
    exclude = ['activity', 'donate']


class SectionAdmin(BaseAdmin):
    inlines = [SectionPhotoInline]
