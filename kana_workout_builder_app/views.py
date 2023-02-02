from django.shortcuts import render
from .models import Workout, Exercise


def index(request):
    """The home page for Kana Workout Builder"""
    return render(request, "kana_workout_builder_app/index.html")


def workouts(request):
    """Show all workouts"""
    workouts = Workout.objects.order_by("date_added")
    context = {"workouts": workouts}
    return render(request, "kana_workout_builder_app/workouts.html", context)


def workout(request, workout_id):
    """Shows a single workout and all its exercises"""
    workout = Workout.objects.get(id=workout_id)
    exercises = workout.exercise_set.order_by("-date_added")
    context = {"workout": workout, "exercises": exercises}
    return render(request, "kana_workout_builder_app/workout.html", context)
