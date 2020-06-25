from django.shortcuts import render, redirect
from django import forms
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .models import Record

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
