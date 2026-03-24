from django import forms
from django_summernote.widgets import SummernoteWidget

from todo.models import Todo, Comment


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', "type": 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', "type": 'date'}),
            'description': SummernoteWidget(),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed', 'completed_image', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', "type": 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', "type": 'date'}),
            'description': SummernoteWidget(),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'completed_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        labels = {
            'message': '내용'
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'class': "form-control",
                "rows": "3",
                "cols": "50",
                "placeholder": "내용을 입력하세요.",
            })
        }