from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name='file_upload'),
    path('download/<code>/', views.FileDownloadView.as_view(), name='file_download'),
    path('verify-password/<code>/', views.VerifyPasswordView.as_view(), name='verify_password'),
]
