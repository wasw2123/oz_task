from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q, Prefetch
from django.http import Http404, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.forms import CommentForm, TodoForm, TodoUpdateForm
from todo.models import Todo, Comment


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    paginate_by = 10
    ordering = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()

        #superuser 검증
        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        # 검색
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        return queryset

class TodoDetailView(LoginRequiredMixin, DetailView):
    # model = Todo
    queryset = Todo.objects.prefetch_related(
        Prefetch('comments', queryset=Comment.objects.select_related('user').order_by('-created_at'))
    )
    template_name = 'todo/todo_info.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if self.request.user.is_superuser or obj.user == self.request.user:
            return obj

        raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo']=self.object
        context['comment_form'] = CommentForm()
        comment_list = self.object.comments.all()
        paginator = Paginator(comment_list, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'create'
        context['btn_name'] = '생성'
        return context

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoUpdateForm
    template_name = 'todo/todo_form.html'

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        #날짜 선택 위젯
        form.fields['start_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['end_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        return form

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if self.request.user.is_superuser or obj.user == self.request.user:
            return obj
        raise Http404

    def get_success_url(self):
        return reverse('cbv_todo_info', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'update'
        context['btn_name'] = '수정'
        return context


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'


    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if self.request.user.is_superuser or obj.user == self.request.user:
            return obj
        raise Http404

    def get_success_url(self):
        return reverse('cbv_todo_list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['message', ]
    pk_url_kwarg = 'todo_id'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.todo = Todo.objects.get(pk=self.kwargs['todo_id'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cbv_todo_info', kwargs={"pk": self.object.todo.pk})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['message',]

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if self.request.user.is_superuser or obj.user == self.request.user:
            return obj
        raise Http404

    def get_success_url(self):
        return reverse('cbv_todo_info', kwargs={"pk": self.object.todo.pk})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if self.request.user.is_superuser or obj.user == self.request.user:
            return obj
        raise Http404

    def get_success_url(self):
        return reverse('cbv_todo_list')