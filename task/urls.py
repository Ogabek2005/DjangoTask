from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('tasks/' , views.tasks , name='tasks'),
    path('task_detail/<int:id>' , views.task_detail , name='task_detail'),
    path('create_task/' ,views.create_task , name='task_create' ),
    path('update_task/<int:id>' ,views.update_task , name='task_update' ),
    path('delete_task/<int:id>' ,views.delete_task , name='task_delete' ),
]