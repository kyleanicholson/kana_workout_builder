"""Defines URL patterns for kana_workout_builder_app"""
from django.urls import path
from . import views

app_name = "kana_workout_builder_app"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("workouts/", views.workouts, name="workouts"),
    path("workouts/<int:workout_id>/", views.workout, name="workout"),
    path("new_workout/", views.new_workout, name="new_workout"),
    path("new_exercise/<int:workout_id>/", views.new_exercise, name="new_exercise"),
    path("edit_exercise/<int:exercise_id>/", views.edit_exercise, name="edit_exercise"),
]
