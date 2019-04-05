from django.urls import path 

from . import sockets

websocket_urlpatterns = [
  path('ws/notes', sockets.NoteSocket)
]