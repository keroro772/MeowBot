from django.shortcuts import render
from Catnip.models import Catnip

def index(request):
    user_catnip = Catnip.objects.filter(name=request.user)
    return render(request, 'ranks/index.html', {'user_catnip':user_catnip,})