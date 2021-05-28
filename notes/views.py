from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Notes

# Create your views here.
def index(request):
    latest_quick_notes = Notes.objects.order_by('-pub_date')[:5]
    context = {'latest_quick_notes': latest_quick_notes}
    return render(request, 'notes/index.html', context)

def note(request, id):
    note = get_object_or_404(Notes, pk=id)
    return render(request, 'notes/note.html', {'note': note})
