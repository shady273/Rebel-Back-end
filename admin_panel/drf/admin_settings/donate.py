from django.contrib import admin
from django import forms

from drf.admin_settings.base import BaseAdmin
from drf.models.photo import Photo


class PhotoInlineForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        help_texts = {
            'photo': 'Додайте фото з необхідними розмірами та співвідношенням сторін.'
        }


class DonatePhotoInline(admin.StackedInline):
    model = Photo
    exclude = ['activity', 'section', 'merch']
    max_num = 1
    form = PhotoInlineForm


class DonateAdmin(BaseAdmin):
    inlines = [DonatePhotoInline]
