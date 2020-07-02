from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import (
    HomePageView,
    SubmitReportView,
    SubmitSuccessView,
    ReportPageView,
    report_view,
    download_report,
    edit_review,
)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('submit', SubmitReportView.as_view(), name = 'submit_report'),    
    path('success', SubmitSuccessView.as_view(), name = 'submit_success'),
    path('report/', report_view, name = 'report_home'), 
    path(r'report/download/<int:year>/<int:month>/<int:day>/<slug:slug>', download_report , name = 'download_report'),
    path('report/<slug:designation>/<int:pk>/', edit_review, name = 'edit_review'),
]
