from drf.admin_settings.base import BaseAdmin, BasePhotoInline
from drf.models.photo import Photo


class SectionPhotoInline(BasePhotoInline):
    model = Photo
    fk_name = 'section'
    exclude = ['activity', 'donate']


class SectionAdmin(BaseAdmin):
    inlines = [SectionPhotoInline]
