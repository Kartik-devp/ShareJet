from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/auth/', include('accounts.urls')),
    path('api/transfers/', include('transfers.urls')),
    path('api/files/', include('files.urls')),
]

