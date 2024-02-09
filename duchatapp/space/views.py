# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Space

@login_required
def spaces(request):
    spaces = Space.objects.all()

    return render(request, 'space/spaces.html', {'spaces': spaces})

@login_required
def space(request, slug):
    space = Space.objects.get(slug=slug)
    messages = Message.objects.filter(space=space)[0:25]

    return render(request, 'space/space.html', {'space': space, 'messages': messages})