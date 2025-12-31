from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "title", "owner", "is_encrypted", "created_at", "updated_at")
    list_filter = ("is_encrypted", "created_at")
    search_fields = ("title", "content")
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
    class Meta:
        permissions = [
            ("can_view_encrypted_note", "Can view encrypted note content"),
        ]