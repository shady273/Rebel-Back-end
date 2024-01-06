from drf.admin_settings.base import BaseAdmin, BaseInline, PaginatedInline
from drf.models.activity import TextActivity
from drf.models.photo import Photo


class TextActivityInline(BaseInline):
    model = TextActivity
    fk_name = 'text_activity'
    exclude = ['section', 'donate']


class ActivityPhotoInline(PaginatedInline):
    model = Photo
    fk_name = 'activity'
    exclude = ['section', 'donate']


class ActivityAdmin(BaseAdmin):
    inlines = [TextActivityInline, ActivityPhotoInline]