from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes

# Create your views here.
def index(request):
    latest_quick_notes = Notes.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.note_text for q in latest_quick_notes])
    return HttpResponse(output)

def note(request, id):
    response = "You're looking at the note %s."
    return HttpResponse(response % id)
