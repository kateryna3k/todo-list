from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 5
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    paginate_by = 5
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")
