from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_date", "location")
    search_fields = ("name", "location")

    def save_model(self, request, obj, form, change):
        # Validate model (this will invoke clean())
        obj.full_clean()
        super().save_model(request, obj, form, change)
