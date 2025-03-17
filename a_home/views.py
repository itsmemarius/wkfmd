from django.shortcuts import render
from django.conf import settings

def home_view(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})