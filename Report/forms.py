from django import forms
from .models import Record
from django.utils import timezone

OBSERVATIONS = [
    (" ", "-"),
    ("Needs Improvement", "Needs Improvement"),
    ("Satisfactory", "Satisfactory"),
    ("Good", "Good"),
    ("Very Good", "Very Good"),
    ("Excellent", "Excellent"),
    ("Outstanding", "Outstanding"),
]

DESIG = [
    ("all", "All"),
    ("PRT", "PRT"),
    ("TGT", "TGT"),
    ("PGT", "PGT"),
]


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        flds = ['Class', 'teacher', 'section', 'subject', 'total_students', 'present', 'platform', 'topic', 'homework', 'date']
        for fld in flds:
            self.fields[fld].widget.attrs['readonly'] = True

    class Meta:
        model = Record
        fields = '__all__'

class EditReviewForm(forms.Form):
    observation = forms.ChoiceField(choices = OBSERVATIONS)
    remark = forms.CharField(max_length = 100, required = False)


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    designation = forms.ChoiceField(choices = DESIG)
