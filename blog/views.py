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

def posts_list(request):
    posts_list = Note.objects.order_by('-pub_date')[:5]
    context = {'posts_list': posts_list}
    return render(request, 'blog/posts_list.html', context)

def note(request, id):
    note = get_object_or_404(Note, pk=id)
    comment = Comment.objects.filter(note_id=id).order_by('-id')
    form = CommentForm()
    return render(request, 'blog/note.html', {'note': note, 'comment': comment, 'form': form})

def comments(request):
    if request.is_ajax() and request.method == 'POST':
        comment = Comment(text=request.POST['comment'], note_id=request.POST['id'], pub_date=timezone.now())
        comment.save()
    return HttpResponse('fine')


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
