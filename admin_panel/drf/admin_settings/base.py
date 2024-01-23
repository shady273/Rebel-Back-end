from django.contrib import admin
from django.shortcuts import redirect
from django_admin_inline_paginator.admin import TabularInlinePaginated


class BaseAdmin(admin.ModelAdmin):
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().changeform_view(request, object_id, form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        obj = self.model.objects.first()
        if obj:
            return redirect('admin_panel:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), obj.id)
        else:
            return super().add_view(request, extra_context)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


class BaseInline(admin.StackedInline):

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None:
            return 0
        return 1


class PaginatedInline(TabularInlinePaginated):
    per_page = 5
