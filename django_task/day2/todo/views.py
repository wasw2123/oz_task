from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from todo.forms import TodoForm, TodoUpdateForm
from todo.models import Todo

@login_required()
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')

    q = request.GET.get('q')
    if q:
        todos = todos.filter(Q(title__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(todos, 5)
    page = request.GET.get('page')
    todos_page = paginator.get_page(page)

    context = {
        'todo_list': todos_page,
    }
    return render(request, 'todo/todo_list.html', context)

@login_required()
def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    context = todo.__dict__
    return render(request, 'todo/todo_info.html', context)

@login_required()
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect('todo_info', pk=todo.pk)
    context = {
        "form": form
    }
    return render(request, 'todo/todo_form.html', context)

@login_required()
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_info', pk=todo.pk)
    context = {
        "form": form
    }
    return render(request, 'todo/todo_form.html', context)

@login_required()
@require_http_methods(['POST'])
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')