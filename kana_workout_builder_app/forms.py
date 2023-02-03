from django import forms

from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["title"]
        labels = {"title": ""}


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "sets", "reps", "rpe", "notes"]
        labels = {
            "name": "Name",
            "sets": "Sets",
            "reps": "Reps",
            "rpe": "Target RPE",
            "notes": "Notes",
        }
        widgets = {"notes": forms.Textarea(attrs={"cols": 80})}
