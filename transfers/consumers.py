import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TransferProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_code = self.scope['url_route']['kwargs']['session_code']
        self.room_group_name = f'transfer_{self.session_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        progress = data.get('progress')
        file_name = data.get('file_name')
        action = data.get('action', 'upload')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'progress_update',
                'progress': progress,
                'file_name': file_name,
                'action': action,
            }
        )

    async def progress_update(self, event):
        await self.send(text_data=json.dumps({
            'progress': event['progress'],
            'file_name': event['file_name'],
            'action': event['action'],
        }))

class ClipboardSyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_code = self.scope['url_route']['kwargs']['session_code']
        self.room_group_name = f'clipboard_{self.session_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get('content')

        # Broadcast the new content to all connected clients
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'clipboard_update',
                'content': content
            }
        )

    async def clipboard_update(self, event):
        await self.send(text_data=json.dumps({
            'content': event['content']
        }))
