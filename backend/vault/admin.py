from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "is_encrypted", "created_at", "updated_at")
    list_filter = ("is_encrypted", "created_at")
    search_fields = ("title",)
    readonly_fields = ("id", "title", "owner", "is_encrypted", "created_at", "updated_at")
    exclude = ("content",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True