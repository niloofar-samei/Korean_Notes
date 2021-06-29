from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from .models import Note, Comment
from .forms import CommentForm
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def index(request):
    latest_quick_notes = Note.objects.order_by('-pub_date')[:5]
    context = {'latest_quick_notes': latest_quick_notes}
    return render(request, 'blog/index.html', context)

def note(request, id, message=''):
    note = get_object_or_404(Note, pk=id)
    comment = Comment.objects.filter(note_id=id)
    form = CommentForm()
    return render(request, 'blog/note.html', {'note': note, 'comment': comment, 'message': message, 'form': form})

def comments(request, id):
    try:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.note_id = id
                new_form.pub_date = timezone.now()
                new_form.save()
            return HttpResponseRedirect(reverse('blog:note', args=(id, "successful")))
    except:
        raise Http404("not exist")

def like(request):
    if request.is_ajax() and request.method == 'POST':
        print(request.POST['color'])
        note = get_object_or_404(Note, id=request.POST['id'])
        print(note.like)
        if request.POST['color'] == 'red':
            note.like += 1
        else:
            if note.like != 0:
                note.like -= 1
        print(note.like)
        Note.objects.filter(id=1).update(like=note.like)
        return HttpResponse(note.like)
        #resp_data = {
        #    'text': note.like,
        #}
        #return JsonResponse(resp_data, status=200)
