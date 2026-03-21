from django import forms
from django.urls import reverse
from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView

from todo.models import Todo


class TodoListView(ListView):
    model = Todo
    paginate_by = 5
    ordering = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()

        #staff 검증
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)

        # 검색
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        return queryset

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_info.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if self.request.user.is_staff or obj.user == self.request.user:
            return obj

        raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.object.__dict__)
        return context


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
    template_name = 'todo/todo_create.html'

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        #날짜 선택 위젯
        form.fields['start_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['end_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cbv_todo_info', kwargs={"pk": self.object.pk})





