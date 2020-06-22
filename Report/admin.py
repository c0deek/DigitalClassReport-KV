from django.contrib import admin
from .models import (
    Teacher, 
    Record,
)

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Record)
