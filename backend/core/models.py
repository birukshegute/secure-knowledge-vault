from django.conf import settings
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_encrypted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_display_content(self, user):
            if self.is_encrypted and not user.has_perm("core.can_view_encrypted_note"):
                return "[ENCRYPTED]"
            return self.content
    
    class Meta:
        permissions = [
            ("can_view_encrypted_note", "Can view encrypted note content"),
        ]
