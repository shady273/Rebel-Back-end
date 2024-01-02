from django.contrib import admin

from drf.admin_settings.base import BaseAdmin
from drf.models.activity import TextActivity
from drf.models.photo import Photo


class TextActivityInline(admin.StackedInline):
    model = TextActivity
    extra = 1
    fk_name = 'text_activity'
    exclude = ['section', 'donate']


class ActivityPhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    fk_name = 'activity'
    exclude = ['section', 'donate']


class ActivityAdmin(BaseAdmin):
    inlines = [TextActivityInline, ActivityPhotoInline]