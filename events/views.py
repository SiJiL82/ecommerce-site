from django.shortcuts import (
    redirect,
    render,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        new_event_form = NewEventForm(data=request.POST)
        if new_event_form.is_valid():
            new_event_form.save()
            messages.success(request, 'New event saved successfully!')

    return render(request, 'events/events.html', context)


@login_required
def remove_event(request, eventid):
    """Remove the event """

    if not request.user.is_superuser:
        return redirect(reverse('events'))

    try:
        event = get_object_or_404(Event, pk=eventid)
        event.delete()
        messages.info(request, 'Event deleted')
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
