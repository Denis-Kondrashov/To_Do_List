from django.views.generic import ListView, DetailView, CreateView
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
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')
