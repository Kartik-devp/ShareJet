from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileItem
from transfers.models import TransferSession
from .serializers import FileItemSerializer
from django.shortcuts import get_object_or_404

class FileUploadView(generics.CreateAPIView):
    serializer_class = FileItemSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        session_code = request.data.get('transfer_code')
        session = get_object_or_404(TransferSession, transfer_code=session_code)
        
        if session.is_expired():
            return Response({'error': 'Session expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        file_item = FileItem.objects.create(
            session=session,
            file=file_obj,
            file_name=file_obj.name,
            file_size=file_obj.size,
            file_type=file_obj.content_type or 'application/octet-stream'
        )
        return Response(FileItemSerializer(file_item).data, status=status.HTTP_201_CREATED)

class FileDownloadView(generics.RetrieveAPIView):
    # This view simply retrieves file details so frontend can show them (preview etc)
    # The actual stream will be served via media url or a separate stream view
    serializer_class = FileItemSerializer

    def get(self, request, code, *args, **kwargs):
        session = get_object_or_404(TransferSession, transfer_code=code)
        if session.is_expired():
            return Response({'error': 'Session expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        # In a real app we might handle password here if requested in headers
        files = session.files.all()
        return Response(FileItemSerializer(files, many=True).data, status=status.HTTP_200_OK)

class VerifyPasswordView(generics.GenericAPIView):
    def post(self, request, code, *args, **kwargs):
        session = get_object_or_404(TransferSession, transfer_code=code)
        password = request.data.get('password')
        if session.password_hash and session.password_hash != password:
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

