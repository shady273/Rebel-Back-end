from django.contrib import admin
from django import forms
from PIL import Image

from drf.models.support import Support


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = '__all__'

    def clean_logo(self):
        logo = self.cleaned_data['logo']
        max_size = (64, 64)
        error_message = (f'Будь ласка, завантажуйте зображення розміром {max_size[0]}px на {max_size[1]}px '
                         f'та у форматі PNG.')
        image = Image.open(logo)
        if image.size != max_size:
            raise forms.ValidationError(error_message)

        if not logo.name.lower().endswith(('.png', '.PNG')):
            raise forms.ValidationError(error_message)
        return logo


class SupportAdmin(admin.ModelAdmin):
    form = SupportForm

