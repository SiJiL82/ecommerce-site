from django.shortcuts import render
from .models import Event
from datetime import datetime, timedelta

def view_events(request):
  """ A view that renders the events page """

  now = datetime.now()
  end_date = now + timedelta(days=730)
  future_events = Event.objects.filter(date__range=[now, end_date])
  ordered_events = future_events.order_by('date')

  context = {
    'events': ordered_events
  }

  return render(request, 'events/events.html', context)
