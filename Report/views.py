from django.shortcuts import render, redirect
from django import forms
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from modules import print_xl 

import datetime
import os

from .models import Teacher, Record

#Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SubmitReportView(CreateView):
    model = Record
    template_name = 'submit.html'
    fields = ['teacher',
              'date',
              'Class',
              'section',
              'subject',
              'total_students',
              'present',
              'topic',
              'platform',
              'homework',
    ]
    success_url = reverse_lazy('submit_success')

class SubmitSuccessView(TemplateView):
    template_name = 'submit_success.html'
   

class ReportPageView(TemplateView):
    template_name = 'report_home.html'

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

def report_view(request):
    report_date = request.GET.get('date', '')
    if(report_date):
        data = list(Record.objects.filter(date = report_date))
        print(data)
        return render(request, 'report_show.html', {'data': data})
    else:
        form = DateForm()
        return render(request, 'report_home.html', {'form': form})


def download_report(request, year, month, day):
    date = datetime.date(int(year), int(month), int(day))
    data = list(Record.objects.filter(date = date))
    for entry in data:
        print(entry)

    data_json = serializers.serialize('json', Record.objects.filter(date = date))
    teachers_json = serializers.serialize('json', Teacher.objects.all())
    print_xl.generate_xl(data_json, teachers_json)


    file_path = os.path.join(settings.MEDIA_ROOT, 'report.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
