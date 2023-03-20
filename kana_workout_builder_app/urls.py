"""Defines URL patterns for kana_workout_builder_app"""
from django.urls import path
from . import views

app_name = "kana_workout_builder_app"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("workouts/", views.workouts, name="workouts"),
    path("workouts/<int:workout_id>/", views.workout, name="workout"),
    path("new_workout/<int:program_id>", views.new_workout, name="new_workout"),
    path("new_exercise/<int:workout_id>/", views.new_exercise, name="new_exercise"),
    path("edit_exercise/<int:exercise_id>/", views.edit_exercise, name="edit_exercise"),
    path("programs/", views.programs, name="programs"),
    path("programs/<int:program_id>/", views.program, name="program"),
    path(
        "programs/edit_program/<int:program_id>",
        views.edit_program,
        name="edit_program",
    ),
    path("new_program/", views.new_program, name="new_program"),
    path(
        "programs/delete_program/<int:program_id>",
        views.delete_program,
        name="delete_program",
    ),
]

# TODO: edit_workout
