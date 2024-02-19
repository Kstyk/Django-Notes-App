from django import forms
from .models import Note
from django.utils import timezone


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter title...'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea textarea-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter content...', 'rows': 10}))

    class Meta:
        model = Note
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        instance = super(NoteForm, self).save(commit=False)
        if not instance.pk:
            instance.created_at = timezone.now()
        instance.updated_at = timezone.now()

        if commit:
            instance.save()
        return instance
