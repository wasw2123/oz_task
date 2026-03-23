from django import forms

from todo.models import Todo, Comment


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