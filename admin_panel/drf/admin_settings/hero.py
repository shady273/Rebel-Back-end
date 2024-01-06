from drf.admin_settings.base import BaseAdmin, BaseInline
from drf.models.photo import Photo


class SectionPhotoInline(BaseInline):
    model = Photo
    fk_name = 'section'
    exclude = ['activity', 'donate', 'merch']


class SectionAdmin(BaseAdmin):
    inlines = [SectionPhotoInline]
