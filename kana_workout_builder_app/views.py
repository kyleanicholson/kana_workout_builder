from django.shortcuts import render, redirect
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm


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


def new_workout(request):
    """Add a new workout"""
    if request.method != "POST":
        # No data submitted, create blank form
        form = WorkoutForm()
    else:
        # POST data submitted; process data
        form = WorkoutForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("kana_workout_builder_app:workouts")
    # Display a blank or invalid form
    context = {"form": form}
    return render(request, "kana_workout_builder_app/new_workout.html", context)


def new_exercise(request, workout_id):
    """Add a new exercise for a particular workout"""
    workout = Workout.objects.get(id=workout_id)
    if request.method != "POST":
        # No data submitted; create blank form.
        form = ExerciseForm()
    else:
        # POST data submitted, process data
        form = ExerciseForm(data=request.POST)
        if form.is_valid():
            new_exercise = form.save(commit=False)
            new_exercise.workout = workout
            new_exercise.save()
            return redirect("kana_workout_builder_app:workout", workout_id=workout_id)
    # Display a blank or invalid form.
    context = {"workout": workout, "form": form}
    return render(request, "kana_workout_builder_app/new_exercise.html", context)


def edit_exercise(request, exercise_id):
    """Edit an existing exercise"""
    exercise = Exercise.objects.get(id=exercise_id)
    workout = exercise.workout

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry
        form = ExerciseForm(instance=exercise)
    else:
        # POST data submitted; process data.
        form = ExerciseForm(instance=exercise, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("kana_workout_builder_app:workout", workout_id=workout.id)
    context = {"exercise": exercise, "workout": workout, "form": form}
    return render(request, "kana_workout_builder_app/edit_exercise.html", context)
