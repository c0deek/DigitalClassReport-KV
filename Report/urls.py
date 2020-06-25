from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import (
    HomePageView,
    SubmitReportView,
    SubmitSuccessView,
    ReportPageView,
    report_view,
)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('submit', SubmitReportView.as_view(), name = 'submit_report'),    
    path('success', SubmitSuccessView.as_view(), name = 'submit_success'),
    re_path(r'^report/$', report_view, name = 'report_home'), 
]
