from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
DESIGNATIONS = [
    ("PRT", "prt"),
]

class Teachers(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    designation = models.CharField(max_length=3, choices=DESIGNATIONS)

class Record(models.Model):
    class_name = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    section = models.CharField(max_length = 3)
    subject = models.CharField(max_length = 20)
    no_students = models.IntegerField(default = 0)
    platform = models.CharField(max_length = 20)
