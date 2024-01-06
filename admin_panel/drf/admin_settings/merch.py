from drf.admin_settings.base import BaseAdmin, BaseInline
from drf.models.photo import Photo


class MerchPhotoInline(BaseInline):
    model = Photo
    exclude = ['activity', 'donate', 'section']


class MerchAdmin(BaseAdmin):
    inlines = [MerchPhotoInline]