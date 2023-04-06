from django import forms
from .models import Workout, Exercise, Program
from django.forms import formset_factory


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ["title", "goal", "days_per_week", "description"]
        labels = {
            "title": "Title",
            "goal": "Training Goal",
            "days_per_week": "Days Per Week",
            "description": "Description",
        }
        widgets = {"days_per_week": forms.NumberInput(attrs={"max": "7"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs["class"] = "form-control"


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["title"]
        labels = {"title": ""}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs["class"] = "form-control"


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "sets", "reps", "rpe", "rest"]
        labels = {
            "name": "Name",
            "sets": "Sets",
            "reps": "Reps",
            "rpe": "Target RPE",
            "rest": "Rest (minutes)",
        }
        widgets = {"rpe": forms.NumberInput(attrs={"max": "10"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {"class": "form-control"}
            self.fields[str(field)].widget.attrs.update(new_data)


ExerciseFormSet = formset_factory(ExerciseForm, extra=1)
