from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Program(models.Model):
    """A training program created by the user"""

    PROGRAM_GOALS = (
        ("MG", "Muscle Gain"),
        ("ST", "Strength Gain"),
        ("PB", "Powerbuilding"),
        ("SP", "Sports Performance"),
        ("GE", "General Health and Fitness"),
        ("OT", "Other"),
    )

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=2, choices=PROGRAM_GOALS)
    days_per_week = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    notes = models.TextField(null=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Workout(models.Model):
    """A Workout created by the user"""

    program = models.ForeignKey(Program, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

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


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
