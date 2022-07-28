from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from .models import Event
from datetime import datetime, timedelta
from .forms import NewEventForm

def view_events(request):
  """ A view that renders the events page """

  now = datetime.now()
  end_date = now + timedelta(days=730)
  future_events = Event.objects.filter(date__range=[now, end_date])
  ordered_events = future_events.order_by('date')

  context = {
    'events': ordered_events,
    'new_event_form': NewEventForm()
  }

  if request.method == 'POST':
    print("Posted form")
    new_event_form = NewEventForm(data=request.POST)
    if new_event_form.is_valid():
      new_event_form.save()
    return render(request, 'events/events.html', context)
  else:
    return render(request, 'events/events.html', context)

def remove_event(request, eventid):
  """Remove the event """

  try:
    event = get_object_or_404(Event, pk=eventid)
    event.delete()
    return HttpResponse(status=200)
  except Exception as e:
    return HttpResponse(status=500)