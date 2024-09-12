from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'MyApp/task_list.html'
    context_object_name = 'MyApp'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'MyApp/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'MyApp/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'MyApp/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'MyApp/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
