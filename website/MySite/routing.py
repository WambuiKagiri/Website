# chat/routing.py
from django.conf.urls import url

from .consumers import ChatConsumer

websocket_urlpatterns = [
    url(r'message/$', ChatConsumer, name='chat'),
]


