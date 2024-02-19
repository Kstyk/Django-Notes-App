from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
# Create your views here.


@login_required
def home(request):
    return render(request, 'notes/index.html')


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.author = request.user
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})
