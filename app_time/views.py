from django.shortcuts import render
from django.utils import timezone
import pytz



def time_wold(request):
    now = timezone.now()
    context = {'now':now,'time_zones':pytz.all_timezones}
    template = 'time_world.html'
    return render(request,template,context)

