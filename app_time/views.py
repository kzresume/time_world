from django.shortcuts import render
from django.utils import timezone
import pytz



def time_wold(request):
    value = False
    if request.GET.get('text'):
        value = request.GET.get('text') 
    now = timezone.now()
    context = {'now':now, 'time_zones':pytz.all_timezones,'value':value}
    template = 'time_world.html'
    return render(request,template,context)

