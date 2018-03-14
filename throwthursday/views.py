from django.shortcuts import render
from .models import Throw
from Catnip.models import Catnip
from django.http import HttpResponseRedirect

def index(request):
    all_throw = Throw.objects.all()
    user_catnip = Catnip.objects.filter(name=request.user)
    throw_names = Throw.objects.values_list('name')
    return render(request, 'throwthursday/index.html', {'all_throw': all_throw,'user_catnip':user_catnip,'throw_names':throw_names})

def sign_up(request):
    y=[]
    for x in Throw.objects.all():
        y.append(x.name)
    if not request.user.username in y:
        a = Throw()
        a.name = request.user
        a.save()
    return HttpResponseRedirect('http://mrmeowchow.com/Throwdown/')

def Remove_self(request):
    y=[]
    for x in Throw.objects.all():
        y.append(x.name)
    if request.user.username in y:
        username = request.user.username
        Throw.objects.filter(name=username).delete()
    return HttpResponseRedirect('http://mrmeowchow.com/Throwdown/')