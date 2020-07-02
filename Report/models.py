from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
DESIGNATIONS = [
    ("PRT", "PRT"),
    ("TGT", "TGT"),
    ("PGT", "PGT"),
    ("HM", "HM"),
    ("VP", "VP"),
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
    ("D", "D"),
]

CLASS_ROMANS = [
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
    ("VIII", "VIII"),
    ("IX", "IX"),
    ("X", "X"),
    ("XI", "XI"),
    ("XII", "XII"),

]

SUBJECTS = [
    ("Mathematics", "Mathematics"),
    ("Hindi", "Hindi"),
    ("English", "English"),
    ("Sanskrit", "Sanskrit"),
    ("Science", "Science"),
    ("Social Science", "Social Science"),
    ("Physics","Physics"),
    ("Chemistry", "Chemistry"),
    ("Biology", "Biology"),
    ("CS", "CS"),
    ("IP", "IP"),
    ("Ph Education", "Ph Education"),
    ("History", "History"),
    ("Geography", "Geography"),
    ("Sociology", "Sociology"),
    ("Accountancy", "Accountancy"),
    ("Business Studiies", "Business Studies"),
    ("Economics", "Economics"),
    ("EVS", "EVS"),
    ("Drawing", "Drawing"),
    ("Music", "Music"),
    ("Games", "Games"),
    ("Library", "Library"),
    ("WE", "WE"),
]

PLATFORMS = [
    ("Zoom", "Zoom"),
    ("Google Meet", "Google Meet"),
    ("WhatsApp", "WhatsApp"),
    ("MS Teams", "MS Teams"),
    ("Zoom + WhatsApp", "Zoom + WhatsApp"),
    ("Google Meet + WhatsApp", "Google Meet + Whatsapp"),
    ("Other", "Other"),
]

class Teacher(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    designation = models.CharField(max_length = 3, choices = DESIGNATIONS)

    def __str__(self):
        return self.name

class Record(models.Model):
    Class = models.CharField(default = "I", max_length = 4, choices = CLASS_ROMANS)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    section = models.CharField(max_length = 1, choices = SECTIONS)
    subject = models.CharField(max_length = 30, choices = SUBJECTS)
    total_students = models.IntegerField(default = 0)
    present = models.IntegerField(default = 0)
    platform = models.CharField(max_length = 30, choices=PLATFORMS)
    topic = models.CharField(max_length = 50)
    homework = models.CharField(max_length = 50)
    date = models.DateField(default = timezone.now)
    observation = models.CharField(max_length = 20, choices = OBSERVATIONS, blank = True)
    remark = models.CharField(default = "-", max_length = 100, blank = True)
    observed_by = models.CharField(blank = True, max_length = 20)

    def __str__(self):
        return f"{self.date}: '{self.teacher}'\t'{self.subject}'\t'{self.Class}'\t'{self.section}'"
