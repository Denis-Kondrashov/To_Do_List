from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from . models import Task
from . forms import TaskForm


class TaskList(ListView):
    model = Task
    template_name = 'base/tasks_list.html'
    context_object_name = 'tasks_list'
    ordering = ['-create']


class TaskDetail(DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task_detail'


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('base:tasks')


def custom_403_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_update.html'
    success_url = reverse_lazy('base:tasks')

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Task, pk=self.kwargs['pk'])
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_detail'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('base:tasks')

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Task, pk=self.kwargs['pk'])
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

