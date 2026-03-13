from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateSessionView.as_view(), name='create_session'),
    path('clipboard/', views.ClipboardSyncView.as_view(), name='clipboard_sync'),
]
