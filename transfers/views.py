from rest_framework import generics, status
from rest_framework.response import Response
from .models import TransferSession, ClipboardItem
from .serializers import TransferSessionSerializer, ClipboardItemSerializer
import random
import string
from django.utils.timezone import now, timedelta

def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class CreateSessionView(generics.CreateAPIView):
    serializer_class = TransferSessionSerializer

    def create(self, request, *args, **kwargs):
        expiry_minutes = int(request.data.get('expiry_minutes', 60))
        password = request.data.get('password', None)
        
        # Simple setup for password, we can hash it if provided
        
        session = TransferSession.objects.create(
            transfer_code=generate_code(),
            expiry_time=now() + timedelta(minutes=expiry_minutes),
            password_hash=password if password else None
        )
        return Response(TransferSessionSerializer(session).data, status=status.HTTP_201_CREATED)

class ClipboardSyncView(generics.CreateAPIView):
    serializer_class = ClipboardItemSerializer

    def create(self, request, *args, **kwargs):
        code = request.data.get('transfer_code')
        content = request.data.get('content')
        try:
            session = TransferSession.objects.get(transfer_code=code)
            if session.is_expired():
                return Response({'error': 'Session expired'}, status=status.HTTP_400_BAD_REQUEST)
            ClipboardItem.objects.create(session=session, content=content)
            # In real-time we would broadcast this via WebSockets
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        except TransferSession.DoesNotExist:
            return Response({'error': 'Invalid code'}, status=status.HTTP_404_NOT_FOUND)

