from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import (
    HomePageView,
    SubmitReportView,
    SubmitSuccessView,
    ReportPageView,
    report_view,
    download_report
)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('submit', SubmitReportView.as_view(), name = 'submit_report'),    
    path('success', SubmitSuccessView.as_view(), name = 'submit_success'),
    path('report/', report_view, name = 'report_home'), 
    re_path(r'report/download/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', download_report , name = 'download_report')
]
