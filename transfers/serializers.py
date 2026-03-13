from rest_framework import serializers
from .models import TransferSession, ClipboardItem

class TransferSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferSession
        fields = ['id', 'transfer_code', 'expiry_time', 'created_at']

class ClipboardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipboardItem
        fields = ['id', 'content', 'created_at']
