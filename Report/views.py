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
from .forms import DateForm, EditReviewForm

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

def report_view(request):
    report_date = request.GET.get('date', '')
    designation = request.GET.get('designation', '')
    if(report_date):
        if(designation == "all"):
            data = list(Record.objects.filter(date = report_date))
            all = True
        else:
            data = list(Record.objects.filter(date = report_date, teacher__designation__contains = designation))
            all = False

        return render(request, 'report_show.html', {'data': data, 'all': all})
    else:
        form = DateForm()
        return render(request, 'report_home.html', {'form': form})


def download_report(request, year, month, day, slug):
    date = datetime.date(int(year), int(month), int(day))
    data = list(Record.objects.filter(date = date))  

    if(slug != 'all'):
        data_json = serializers.serialize('json', Record.objects.filter(date = date, teacher__designation = slug))
    else:
        data_json = serializers.serialize('json', Record.objects.filter(date = date)
    
    teachers_json = serializers.serialize('json', Teacher.objects.all())

    file_path = os.path.join(settings.MEDIA_ROOT, 'report.xlsx')
    if os.path.exists(file_path):
        os.remove(file_path)

    print_xl.generate_xl(data_json, teachers_json)

    print("FROM VIEW", file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def edit_review(request, designation,  pk):
    entry = Record.objects.get(id = pk)
    form = EditReviewForm()
    date = str(entry.date)

    if(request.method == 'POST'):
        observation = request.POST['observation']
        remark = request.POST['remark']
        entry.observation = observation
        entry.remark = remark
        entry.observed_by = request.user.username
        entry.save()
        return redirect(f'/report/?date={date}&designation={designation}')
        return redirect('download_report', date[:4], date[5:7], date[8:], designation)
        
    return render(request, 'edit_review.html', {'entry': entry, 'form': form})
