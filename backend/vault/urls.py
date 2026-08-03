from django.urls import path
from . import views

urlpatterns = [
    path("notes/create/", views.create_note, name="create_note"),
]