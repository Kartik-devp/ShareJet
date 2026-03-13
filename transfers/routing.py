from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/transfer/(?P<session_code>\w+)/$', consumers.TransferProgressConsumer.as_asgi()),
    re_path(r'ws/clipboard/(?P<session_code>\w+)/$', consumers.ClipboardSyncConsumer.as_asgi()),
]
