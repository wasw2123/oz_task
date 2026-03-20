from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView

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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if self.request.user.is_staff or obj.user == self.request.user:
            return obj

        raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.object.__dict__)
        return context





