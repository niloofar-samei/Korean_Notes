from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Notes, Comments

# Create your views here.
def index(request):
    latest_quick_notes = Notes.objects.order_by('-pub_date')[:5]
    context = {'latest_quick_notes': latest_quick_notes}
    return render(request, 'notes/index.html', context)

def note(request, id, message='Leave your comment or ask a question if you have!'):
    note = get_object_or_404(Notes, pk=id)
    return render(request, 'notes/note.html', {'note': note, 'message': message})

def comments(request, id):
    note = get_object_or_404(Notes, pk=id)
    try:
        if request.POST['comments'] != '':
            comment = Comments(comment_text=request.POST['comments'], note_id=id)
            comment.save()
            return HttpResponseRedirect(reverse('notes:note', args=(id, "successful")))
        else:
            note = get_object_or_404(Notes, pk=id)
            return HttpResponseRedirect(reverse('notes:note', args=(id, "unsuccessful")))
    except:
        raise Http404("not exist")
