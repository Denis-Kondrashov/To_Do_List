from django.views.generic import ListView, DetailView

from . models import Task


class TaskList(ListView):
    model = Task
    template_name = 'base/tasks_list.html'
    context_object_name = 'tasks_list'
    ordering = ['-create']


class TaskDetail(DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task_detail'
