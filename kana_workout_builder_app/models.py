from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Workout(models.Model):
    """A Workout created by the user"""

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Exercise(models.Model):
    """An exercise created by the user, associated w/ a workout"""

    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    sets = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    reps = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    rpe = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    notes = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.name[:50]}"
