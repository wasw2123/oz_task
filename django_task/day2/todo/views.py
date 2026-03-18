from django.shortcuts import render, get_object_or_404

from todo.models import Todos


# Create your views here.
def todo_list(request):
    todos = Todos.objects.all()
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