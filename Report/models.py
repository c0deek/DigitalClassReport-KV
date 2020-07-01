from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
DESIGNATIONS = [
    ("PRT", "PRT"),
    ("TGT", "TGT"),
    ("PGT", "PGT"),
]

OBSERVATIONS = [
    (" ", "-"),
    ("Needs Improvement", "Needs Improvement"),
    ("Satisfactory", "Satisfactory"),
    ("Good", "Good"),
    ("Very Good", "Very Good"),
    ("Excellent", "Excellent"),
    ("Outstanding", "Outstanding"),
]

SECTIONS = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
]

CLASS_ROMANS = [
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
]

class Teacher(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    designation = models.CharField(max_length = 3, choices = DESIGNATIONS)

    def __str__(self):
        return self.name

class Record(models.Model):
    Class = models.CharField(default = "I", max_length = 3, choices = CLASS_ROMANS)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    section = models.CharField(max_length = 1, choices = SECTIONS)
    subject = models.CharField(max_length = 20)
    total_students = models.IntegerField(default = 0)
    present = models.IntegerField(default = 0)
    platform = models.CharField(max_length = 20)
    topic = models.CharField(max_length = 50)
    homework = models.CharField(max_length = 50)
    date = models.DateField(default = timezone.now)
    observation = models.CharField(max_length = 20, choices = OBSERVATIONS, blank = True)
    remark = models.CharField(default = "-", max_length = 100, blank = True)

    def __str__(self):
        return f"{self.date}: '{self.teacher}'\t'{self.subject}'\t'{self.Class}'\t'{self.section}'"
