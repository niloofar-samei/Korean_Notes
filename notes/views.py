from django.shortcuts import render
from .models import Notes

# Create your views here.
def index(request):
    latest_quick_notes = Notes.objects.order_by('-pub_date')[:5]
    context = {'latest_quick_notes': latest_quick_notes}
    return render(request, 'notes/index.html', context)

def note(request, id):
    response = "You're looking at the note %s."
    return HttpResponse(response % id)
