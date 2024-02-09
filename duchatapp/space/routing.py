# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:space_name>/', consumers.ChatConsumer.as_asgi()),
]