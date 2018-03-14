from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Catnip
def index(request):
    all_Catnip_list = Catnip.objects.order_by('-amount')
    user_catnip = Catnip.objects.filter(name=request.user)
    filtered_list = all_Catnip_list.exclude(amount__in=[0,1,2,3,4,5,6,7,8,9,10])
    filtered_list = filtered_list.exclude(name__in=["mrmeowchow","mrbotchow","nightbot"])
    
    try:
        query = request.GET.get("q")
    except:
        query = None
        
    if query:
        filtered_list = filtered_list.filter(name=query)
    
    paginator = Paginator(filtered_list, 10) 

    page = request.GET.get('page')
    try:
        all_Catnip_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_Catnip_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_Catnip_page = paginator.page(paginator.num_pages)
    
    return render(request, 'Catnip/index.html', {'all_Catnip': all_Catnip_page,'user_catnip':user_catnip,})