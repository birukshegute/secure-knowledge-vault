from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/create/", views.create_note, name="create_note"),
    path("notes/<int:note_id>/", views.view_note, name="view_note"),
    path("notes/<int:note_id>/edit/", views.edit_note, name="edit_note"),
    path("notes/<int:note_id>/delete/", views.delete_note, name="delete_note"),

    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]