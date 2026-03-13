from django.db import models
from django.utils.timezone import now
import uuid

class TransferSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer_code = models.CharField(max_length=10, unique=True, db_index=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)
    expiry_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return now() > self.expiry_time

class ClipboardItem(models.Model):
    session = models.ForeignKey(TransferSession, on_delete=models.CASCADE, related_name='clipboard_items')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

