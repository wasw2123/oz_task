from django import forms

from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={"type": 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={"type": 'datetime-local'}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={"type": 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={"type": 'datetime-local'}),
        }