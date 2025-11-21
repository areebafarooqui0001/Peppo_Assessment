from django.shortcuts import render, get_object_or_404  # type: ignore
from .models import Event
from django.utils import timezone  # type: ignore


def event_list(request):
    now = timezone.now()
    # Viewer: see ongoing/upcoming events only (event_date >= now)
    events = Event.objects.filter(event_date__gte=now).order_by("event_date")
    return render(request, "events/list.html", {"events": events})


def event_detail(request, pk):
    ev = get_object_or_404(Event, pk=pk)
    return render(request, "events/detail.html", {"event": ev})
