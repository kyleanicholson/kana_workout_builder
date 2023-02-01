from django.shortcuts import render


def index(request):
    """The home page for Kana Workout Builder"""
    return render(request, "kana_workout_builder_app/index.html")
