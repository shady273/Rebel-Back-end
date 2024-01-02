from drf.admin_settings.base import BaseAdmin, BasePhotoInline
from drf.models.activity import TextActivity
from drf.models.photo import Photo


class TextActivityInline(BasePhotoInline):
    model = TextActivity
    fk_name = 'text_activity'
    exclude = ['section', 'donate']


class ActivityPhotoInline(BasePhotoInline):
    model = Photo
    fk_name = 'activity'
    exclude = ['section', 'donate']


class ActivityAdmin(BaseAdmin):
    inlines = [TextActivityInline, ActivityPhotoInline]