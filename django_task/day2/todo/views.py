from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from todo.forms import TodoForm
from todo.models import Todos

def todo_list(request):
    todos = Todos.objects.all().order_by('-created_at')

    paginator = Paginator(todos, 5)
    page = request.GET.get('page')
    todos_page = paginator.get_page(page)

    context = {
        'todos_page': todos_page,
    }
    return render(request,'todo_list.html', context)

def todo_info(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    context = {
        'todo': todo,
    }
    return render(request,'todo_info.html', context)

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
    return render(request, 'todo_create.html', context)

@login_required()
def todo_update(request, pk):
    todo = get_object_or_404(Todos, pk=pk, user=request.user)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_info', pk=todo.pk)
    context = {
        "form": form
    }
    return render(request, 'todo_update.html', context)

@login_required()
@require_http_methods(['POST'])
def todo_delete(request, pk):
    todo = get_object_or_404(Todos, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')