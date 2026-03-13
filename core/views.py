from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class SendView(TemplateView):
    template_name = 'send.html'

class ReceiveView(TemplateView):
    template_name = 'receive.html'

class ClipboardView(TemplateView):
    template_name = 'clipboard.html'

class DownloadView(TemplateView):
    template_name = 'download.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['code'] = self.kwargs.get('code', '')
        return context

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'


