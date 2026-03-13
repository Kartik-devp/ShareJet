from django.db import models
from files.models import FileItem

class DownloadLog(models.Model):
    file_item = models.ForeignKey(FileItem, on_delete=models.CASCADE, related_name='downloads')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    downloaded_at = models.DateTimeField(auto_now_add=True)

