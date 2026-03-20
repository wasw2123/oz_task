from django.urls import path

from todo.cb_views import TodoListView, TodoDetailView

urlpatterns = [
    path('todo/', TodoListView.as_view(), name='cbv_todo_list'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='cbv_todo_detail'),
]