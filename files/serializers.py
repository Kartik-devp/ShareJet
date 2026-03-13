from rest_framework import serializers
from .models import FileItem
from transfers.serializers import TransferSessionSerializer

class FileItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileItem
        fields = ['id', 'file_name', 'file_size', 'file_type', 'created_at', 'session']
