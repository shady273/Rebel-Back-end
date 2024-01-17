from django.contrib import admin
from django import forms

from drf.admin_settings.base import BaseAdmin
from drf.models.photo import Photo


class PhotoInlineForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image.name.lower().endswith(('.png', '.PNG')):
            raise forms.ValidationError('Будь ласка, завантажуйте тільки зображення у форматі PNG.')
        return image


class DonatePhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    exclude = ['activity', 'section', 'merch']
    max_num = 1
    form = PhotoInlineForm


class DonateAdmin(BaseAdmin):
    inlines = [DonatePhotoInline]
