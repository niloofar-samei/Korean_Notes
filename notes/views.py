from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from .models import Notes, Comments
from .forms import CommentForm

# Create your views here.
def index(request):
    latest_quick_notes = Notes.objects.order_by('-pub_date')[:5]
    context = {'latest_quick_notes': latest_quick_notes}
    return render(request, 'notes/index.html', context)

def note(request, id, message=''):
    note = get_object_or_404(Notes, pk=id)
    form = CommentForm()
    return render(request, 'notes/note.html', {'note': note, 'message': message, 'form': form})

def comments(request, id):
    note = get_object_or_404(Notes, pk=id)
    try:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comments(text=form.cleaned_data['comment'], note_id=id)
                comment.save()
            return HttpResponseRedirect(reverse('notes:note', args=(id, "successful")))
    except:
        raise Http404("not exist")
