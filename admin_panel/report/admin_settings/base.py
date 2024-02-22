from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        max_records = 3

        if self.model.objects.count() >= max_records:
            return False
        return super().has_add_permission(request)

