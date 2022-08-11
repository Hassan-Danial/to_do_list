from django.urls import path
from .views import task_detail, task_list, create_task, task_update, task_delete


urlpatterns = [
    path('', task_list.as_view(), name='tasks'),
    path('task/<int:pk>/', task_detail.as_view(), name='task'),
    path('task_create/', create_task.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', task_update.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', task_delete.as_view(), name='task-delete'),
]
