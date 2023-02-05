from django import forms

from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["title"]
        labels = {"title": ""}


class ExerciseForm(forms.ModelForm):
    required_css_class = "required-field"

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
        widgets = {"rpe": forms.NumberInput(attrs={"max": "10"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {"class": "form-control"}
            self.fields[str(field)].widget.attrs.update(new_data)
