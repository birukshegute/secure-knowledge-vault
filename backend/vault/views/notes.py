from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import NoteForm


@login_required
def create_note(request):

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)

            note.owner = request.user

            note.save()

            return redirect("home")

    else:
        form = NoteForm()

    return render(
        request,
        "vault/notes/create.html",
        {"form": form},
    )