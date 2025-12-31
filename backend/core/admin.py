from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = (
        "owner",
        "title",
        "content",
        "is_encrypted",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "title", "owner", "is_encrypted", "created_at", "updated_at")
    list_filter = ("is_encrypted", "created_at")
    search_fields = ("title", "content")
