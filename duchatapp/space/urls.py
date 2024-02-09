# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.urls import path

from . import views

urlpatterns = [
    path('', views.spaces, name='spaces'),
    path('<slug:slug>/', views.space, name='space'),
]