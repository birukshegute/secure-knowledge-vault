from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note



@login_required
def create_note(request):

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)

            note.owner = request.user

            note.save()

            return redirect("create_note")

    else:
        form = NoteForm()

    return render(
        request,
        "vault/create_note.html",
        {"form": form},
    )
@login_required
def dashboard(request):

    notes = Note.objects.filter(
        owner=request.user
    ).order_by("-updated_at")

    return render(
        request,
        "vault/dashboard.html",
        {
            "notes": notes
        }
    )