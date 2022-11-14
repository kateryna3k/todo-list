from django.urls import path
from .views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    change_task_status,
)


urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-status/", change_task_status, name="change-task-status"),

]

app_name = "todo"
