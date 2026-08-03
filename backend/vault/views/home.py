from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Note

@login_required
def home(request):

    notes = Note.objects.filter(
        owner=request.user
    ).order_by("-updated_at")

    return render(
        request,
        "vault/homepage.html",
        {
            "notes": notes
        }
    )