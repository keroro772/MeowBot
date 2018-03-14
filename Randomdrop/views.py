from django.shortcuts import render
from Catnip.models import Catnip
from .models import RandomDrops
def index(request):
    all_drops = RandomDrops.objects.order_by('-price')
    user_catnip = Catnip.objects.filter(name=request.user)
    return render(request, 'Randomdrop/index.html', {'all_drops': all_drops,'user_catnip':user_catnip,})