from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
DESIGNATIONS = [
    ("prt", "PRT"),
]

class Teacher(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    designation = models.CharField(max_length=3, choices=DESIGNATIONS)

    def __str__(self):
        return self.name

class Record(models.Model):
    Class = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    section = models.CharField(max_length = 3)
    subject = models.CharField(max_length = 20)
    total_students = models.IntegerField(default = 0)
    present = models.IntegerField(default = 0)
    platform = models.CharField(max_length = 20)
    topic = models.CharField(max_length = 200)
    homework = models.TextField()
    date = models.DateField(default = timezone.now)

    def __str__(self):
        return f"{self.date}: '{self.teacher}'\t'{self.subject}'\t'{self.Class}'\t'{self.section}'"
