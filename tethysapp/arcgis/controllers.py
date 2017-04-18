from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import TextInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'arcgis/home.html', context)

def map(request):
    """
    Controller for the app map page.
    """
    context = {}

    return render(request, 'arcgis/map.html', context)
