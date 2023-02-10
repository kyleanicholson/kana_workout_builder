from django.shortcuts import render, redirect
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """The home page for Kana Workout Builder"""
    return render(request, "kana_workout_builder_app/index.html")


def about(request):
    """The about page for Kana Workout Builder"""
    return render(request, "kana_workout_builder_app/about.html")


@login_required
def workouts(request):
    """Show all workouts"""
    workouts = Workout.objects.filter(owner=request.user).order_by("date_added")
    context = {"workouts": workouts}
    return render(request, "kana_workout_builder_app/workouts.html", context)


@login_required
def workout(request, workout_id):
    """Shows a single workout and all its exercises"""
    workout = Workout.objects.get(id=workout_id)
    # Make sure the topic belongs to the current user.
    if workout.owner != request.user:
        raise Http404
    exercises = workout.exercise_set.order_by("-date_added")
    context = {"workout": workout, "exercises": exercises}
    return render(request, "kana_workout_builder_app/workout.html", context)


@login_required
def new_workout(request):
    """Add a new workout"""
    if request.method != "POST":
        # No data submitted, create blank form
        form = WorkoutForm()
    else:
        # POST data submitted; process data
        form = WorkoutForm(data=request.POST)
        if form.is_valid():
            new_workout = form.save(commit=False)
            new_workout.owner = request.user
            new_workout.save()
            return redirect("kana_workout_builder_app:workouts")
    # Display a blank or invalid form
    context = {"form": form}
    return render(request, "kana_workout_builder_app/new_workout.html", context)


@login_required
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


@login_required
def edit_exercise(request, exercise_id):
    """Edit an existing exercise"""
    exercise = Exercise.objects.get(id=exercise_id)
    workout = exercise.workout
    if workout.owner != request.user:
        raise Http404

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
