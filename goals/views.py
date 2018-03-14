from django.shortcuts import render
from Catnip.models import Catnip
from .models import goals

from django.http import HttpResponseRedirect

def index(request):
    user_catnip = Catnip.objects.filter(name=request.user)
    goals_list = goals.objects.order_by('-price')
    
    if request.method == 'POST':
        form = request.POST
        current_goal = goals.objects.filter(pk=int(form['pk']))
        try:
            number = int(form['value'])
        except Exception:
            number = 0
        temp = 0
       
        for x in current_goal:
            temp = x.total + number
            if temp > x.price:
                temp -= x.price
                number -= temp
            x.total += number
            x.save()
            
            for y in user_catnip:
                y.currentAmount -= number
                y.save()
        return HttpResponseRedirect("/goals/")
        
    return render(request, 'goals/index.html', {'goals': goals_list,'user_catnip':user_catnip,})
