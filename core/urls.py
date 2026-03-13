from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('send/', views.SendView.as_view(), name='send'),
    path('receive/', views.ReceiveView.as_view(), name='receive'),
    path('clipboard/', views.ClipboardView.as_view(), name='clipboard'),
    path('download/<code>/', views.DownloadView.as_view(), name='download_view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LoginView.as_view(), name='logout'), # Placeholder for simple logout
    path('register/', views.RegisterView.as_view(), name='register'),
]

