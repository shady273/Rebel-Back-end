from django.contrib import admin
from django import forms

from drf.admin_settings.base import BaseAdmin
from drf.models.photo import Photo


class PNGFilter(admin.SimpleListFilter):
    title = 'Format'
    parameter_name = 'format'

    def lookups(self, request, model_admin):
        return (
            ('png', 'PNG'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'png':
            return queryset.filter(image__endswith='.png')


class PhotoInlineForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image.name.lower().endswith('.png'):
            raise forms.ValidationError('Please upload only PNG images.')
        return image


class DonatePhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    exclude = ['activity', 'section']
    max_num = 1
    form = PhotoInlineForm


class DonateAdmin(BaseAdmin):
    inlines = [DonatePhotoInline]