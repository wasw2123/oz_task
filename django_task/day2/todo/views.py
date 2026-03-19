from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from todo.forms import TodoForm
from todo.models import Todos

def todo_list(request):
    todos = Todos.objects.all().order_by('-created_at')
    if not todos:
        raise Http404
    context = {
        'todos': todos,
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