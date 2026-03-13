from django.db import models
import uuid
from transfers.models import TransferSession

def upload_to_path(instance, filename):
    return f"transfers/{instance.session.id}/{filename}"

class FileItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(TransferSession, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=upload_to_path)
    file_name = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

