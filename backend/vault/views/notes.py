from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms import NoteForm
from ..models import Note


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

@login_required
def view_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        owner=request.user
    )

    return render(
        request,
        "vault/notes/detail.html",
        {"note": note},
    )

@login_required
def edit_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        owner=request.user
    )

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("view_note", note_id=note.id)

    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "vault/notes/edit.html",
        {"form": form, "note": note},
    )

@login_required
def delete_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        owner=request.user
    )

    if request.method == "POST":
        note.delete()
        return redirect("home")

    return render(
        request,
        "vault/notes/delete.html",
        {"note": note},
    )